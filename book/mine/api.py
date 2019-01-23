# Create your views here.
from common.defind_error import CHANGE_PASSWORD_FAIL
from lib.http import render_json
from mine.logic import reset_password, wait_payment, wait_goods, wait_comment, finish_comment, finish_order


def change_password(request):
    '''修改密码'''
    uid = request.user.u_id
    password = request.POST.get('password1')
    psd = request.POST.get('password2')
    if reset_password(uid, password, psd):
        result = {'msg': 'change success'}
        del request.session['uid']
        return render_json(result)
    return render_json({'msg': 'change fail'}, code=CHANGE_PASSWORD_FAIL)


def look_wait_payment(request):
    '''查看未付款订单'''
    uid = request.user.u_id
    result = wait_payment(uid)
    return render_json(result)


def look_wait_goods(request):
    '''查看未收货订单'''
    uid = request.user.u_id
    result = wait_goods(uid)
    return render_json(result)


def look_wait_comments(request):
    '''查看未评价订单'''
    uid = request.user.u_id
    result = wait_comment(uid)
    return render_json(result)


def look_finish_comment(request):
    '''查看已评价订单'''
    uid = request.user.u_id
    result = finish_comment(uid)
    return render_json(result)


def look_finish_order(request):
    '''查看已完成订单'''
    uid = request.user.u_id
    result = finish_order(uid)
    return render_json(result)
