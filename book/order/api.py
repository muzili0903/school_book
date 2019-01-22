# Create your views here.
from lib.http import render_json
from order.logic import non_payment, wait_goods, wait_comment, comment


def order_status1(request):
    '''生成订单，未付款'''
    u_id = request.POST.get('u_id')
    message = request.POST.get('message') or 'None'
    result = non_payment(u_id, message)
    return render_json(result)


def order_status2(request):
    '''已付款,待收货'''
    u_id = request.POST.get('u_id')
    o_id = request.POST.get('o_id')
    result = wait_goods(u_id, o_id)
    return render_json(result)


def order_status3(request):
    '''已收货,待评价'''
    u_id = request.POST.get('u_id')
    o_id = request.POST.get('o_id')
    result = wait_comment(u_id, o_id)
    return render_json(result)


def order_status4(request):
    '''已评价'''
    u_id = request.POST.get('u_id')
    o_id = request.POST.get('o_id')
    result = comment(u_id, o_id)
    return render_json(result)
