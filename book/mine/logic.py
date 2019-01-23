# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-23 上午10:00
@Author  : muzili
@File    : logic
'''
from order.models import Order
from user.logic import check_password
from user.models import User


def reset_password(uid, password, psd):
    if check_password(password, psd):
        User.objects.filter(u_id=uid).update(u_password=password)
        return True
    return False


def wait_payment(uid):
    orders = Order.objects.filter(u_id=uid, o_status=1)
    return [order.to_dict() for order in orders]


def wait_goods(uid):
    orders = Order.objects.filter(u_id=uid, o_status=2)
    return [order.to_dict() for order in orders]


def wait_comment(uid):
    orders = Order.objects.filter(u_id=uid, o_status=3)
    return [order.to_dict() for order in orders]


def finish_comment(uid):
    orders = Order.objects.filter(u_id=uid, o_status=4)
    return [order.to_dict() for order in orders]


def finish_order(uid):
    orders = Order.objects.filter(u_id=uid, o_status__in=[3, 4])
    return [order.to_dict() for order in orders]
