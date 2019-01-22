# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-22 下午4:05
@Author  : muzili
@File    : logic
'''
from cart.models import Cart, CartHistory
from order.models import Order
from user.logic import produce_id


def non_payment(u_id, message):
    '''未付款'''
    cart = Cart.mark(u_id)
    oid = produce_id()
    for c in cart['good']:
        CartHistory.objects.create(u_id=c['uid'], g_id=c['gid'], c_num=c['num'],
                                   o_id=oid, c_total_price=c['c_total_price'])
    order = Order()
    order.o_id = oid
    order.u_id = u_id
    order.o_message = message
    order.o_total_price = cart['total_price']
    order.o_status = 1
    order.save()
    return order.to_dict()


def wait_goods(uid, oid):
    '''待收货'''
    order = Order.objects.filter(u_id=uid, o_id=oid).first()
    order.o_status = 2
    order.save()
    return order.to_dict()


def wait_comment(uid, oid):
    '''待评价'''
    order = Order.objects.filter(u_id=uid, o_id=oid).first()
    order.o_status = 3
    order.save()
    return order.to_dict()


def comment(uid, oid):
    '''待评价'''
    order = Order.objects.filter(u_id=uid, o_id=oid).first()
    order.o_status = 4
    order.save()
    return order.to_dict()
