# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-21 下午10:18
@Author  : muzili
@File    : logic
'''
from books.models import Goods
from cart.models import Cart


def add_carts(u_id, g_id, num):
    goods = Goods.objects.filter(g_id=g_id)
    good = goods.first()
    carts = Cart.objects.filter(u_id=u_id, g_id=g_id)
    if carts:
        cart = carts.first()
        cart.c_num += int(num)
        cart.c_total_price += int(num) * good.g_price
        cart.save()
    else:
        cart = Cart()
        cart.u_id = u_id
        cart.g_id = g_id
        cart.c_num = int(num)
        cart.c_total_price = int(num) * good.g_price
        cart.save()
    good.g_stock -= int(num)
    good.g_sale += int(num)
    good.save()
    return {'good': {'num': cart.c_num, 'uid': u_id, 'gid': g_id, 'total_price': cart.c_total_price}}


def change_num(u_id, g_id):
    carts = Cart.objects.filter(u_id=u_id, g_id=g_id)
    goods = Goods.objects.filter(g_id=g_id)
    good = goods.first()
    cart = carts.first()
    return good, cart


def add_num(u_id, g_id):
    good, cart = change_num(u_id, g_id)
    cart.c_num += 1
    cart.c_total_price += good.g_price
    cart.save()
    good.g_stock -= 1
    good.g_sale += 1
    good.save()
    return {'good': {'num': cart.c_num, 'uid': u_id, 'gid': g_id, 'total_price': cart.c_total_price}}


def reduce_num(u_id, g_id):
    good, cart = change_num(u_id, g_id)
    if cart.c_num == 1:
        pass
    else:
        cart.c_num -= 1
        cart.c_total_price -= good.g_price
    cart.save()
    good.g_stock += 1
    good.g_sale -= 1
    good.save()
    return {'good': {'num': cart.c_num, 'uid': u_id, 'gid': g_id, 'total_price': cart.c_total_price}}


def select_good(u_id, g_id, select):
    if select != '0':
        Cart.objects.filter(u_id=u_id, g_id=g_id).update(c_is_delete=1)
    else:
        Cart.objects.filter(u_id=u_id, g_id=g_id).update(c_is_delete=0)
    carts = Cart.objects.filter(c_is_delete=1)
    goods = []
    total_price = 0
    for cart in carts:
        goods.append(cart.to_dict())
        total_price += cart.c_total_price
    return {'good': goods, 'total_price': total_price}


def all_select_good(u_id, select):
    if select != '0':
        Cart.objects.filter(u_id=u_id).update(c_is_delete=1)
    else:
        Cart.objects.filter(u_id=u_id).update(c_is_delete=0)
    carts = Cart.objects.filter(c_is_delete=1)
    goods = []
    total_price = 0
    for cart in carts:
        goods.append(cart.to_dict())
        total_price += cart.c_total_price
    return {'good': goods, 'total_price': total_price}


def is_delete(u_id, g_id):
    good, cart = change_num(u_id, g_id)
    good.g_stock += cart.c_num
    good.g_sale -= cart.c_num
    good.save()
    cart.delete()
    return None