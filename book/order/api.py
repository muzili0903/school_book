# Create your views here.
from lib.http import render_json
from order.logic import non_payment, wait_goods, wait_comment, comment, delete_order, delete_all_order


def order_status1(request):
    '''生成订单，未付款'''
    u_id = request.user.u_id
    message = request.POST.get('message') or 'None'
    result = non_payment(u_id, message)
    return render_json(result)


def order_status2(request):
    '''已付款,待收货'''
    u_id = request.user.u_id
    o_id = request.POST.get('o_id')
    result = wait_goods(u_id, o_id)
    return render_json(result)


def order_status3(request):
    '''已收货,待评价'''
    u_id = request.user.u_id
    o_id = request.POST.get('o_id')
    result = wait_comment(u_id, o_id)
    return render_json(result)


def order_status4(request):
    '''已评价'''
    u_id = request.user.u_id
    o_id = request.POST.get('o_id')
    g_id = request.POST.get('g_id')
    com = request.POST.get('comment')
    result = comment(u_id, o_id, g_id, com)
    return render_json(result)


def delete_orders(request):
    '''删除选中订单'''
    u_id = request.user.u_id
    o_id = request.POST.get('o_id')
    result = delete_order(u_id, o_id)
    return render_json(result)


def delete_all_orders(request):
    '''删除所有订单'''
    u_id = request.user.u_id
    result = delete_all_order(u_id)
    return render_json(result)
