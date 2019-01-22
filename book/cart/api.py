# Create your views here.
from cart.logic import add_carts, add_num, reduce_num, select_good, all_select_good, is_delete
from lib.http import render_json


def add_goods_cart(request):
    num = request.POST.get('num')
    g_id = request.POST.get('g_id')
    u_id = request.POST.get('u_id')
    result = add_carts(u_id, g_id, num)
    return render_json(result)


def add_cart_num(request):
    g_id = request.POST.get('g_id')
    u_id = request.POST.get('u_id')
    result = add_num(u_id, g_id)
    return render_json(result)


def reduce_cart_num(request):
    g_id = request.POST.get('g_id')
    u_id = request.POST.get('u_id')
    result = reduce_num(u_id, g_id)
    return render_json(result)


def is_select_good(request):
    g_id = request.POST.get('g_id')
    u_id = request.POST.get('u_id')
    select = request.POST.get('select')
    result = select_good(u_id, g_id, select)
    return render_json(result)


def is_all_select_good(request):
    u_id = request.POST.get('u_id')
    select = request.POST.get('select')
    result = all_select_good(u_id, select)
    return render_json(result)


def is_delete_cart(request):
    g_id = request.POST.get('g_id')
    u_id = request.POST.get('u_id')
    result = is_delete(u_id, g_id)
    return render_json(result)