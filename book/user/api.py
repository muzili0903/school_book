# Create your views here.
from common.defind_error import LOGIN_ERROR
from lib.http import render_json
from user.logic import verify_code, verify_msg, check_code, verify_login
from user.models import User


def send_verify_code(request):
    phone = request.POST.get('phone')
    result = verify_code(phone)
    return render_json(result)


def register(request):
    phone = request.POST.get('phone')
    username = request.POST.get('username')
    password = request.POST.get('password1')
    psd = request.POST.get('password2')
    vcode = request.POST.get('code')
    result = verify_msg(phone, username, password, psd, vcode)
    return render_json(result)


def phone_login(request):
    phone = request.POST.get('phone')
    vcode = request.POST.get('code')
    if check_code(phone, vcode):
        user = User.objects.get(u_phone=phone)
        request.session['uid'] = user.u_id
        return render_json(user.to_dict())
    else:
        return render_json({'msg': 'verify code error'}, code=LOGIN_ERROR)


def user_login(request):
    username = request.POST.get('username')
    vpassword = request.POST.get('password')
    user = verify_login(username, vpassword)
    if user:
        request.session['uid'] = user.u_id
        return render_json(user.to_dict())
    else:
        return render_json({'msg': 'user or password error'}, code=LOGIN_ERROR)
