# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-21 下午8:33
@Author  : muzili
@File    : api
'''
from books.logic import *
from lib.http import render_json


def best_seller(request):
    '''首页-畅销书籍'''
    result = search_book()
    return render_json(result)


def computer_book(request):
    '''首页-计算机与互联网书籍'''
    result = search_computer_book()
    return render_json(result)


def life_book(request):
    '''首页-生活书籍'''
    result = search_life_book()
    return render_json(result)


def success_book(request):
    '''首页-成功励志书籍'''
    result = search_success_book()
    return render_json(result)


def price_ascending_order(request):
    '''价格升序'''
    result = price_ascending()
    return render_json(result)


def price_descending_order(request):
    '''价格降序'''
    result = price_descending()
    return render_json(result)


def sale_descending_order(request):
    '''销量降序'''
    result = sale_descending()
    return render_json(result)


def sort_type_book(request):
    '''按类型分类'''
    g_type = request.GET.get('type')
    resulet = sort_type(g_type)
    return render_json(resulet)
