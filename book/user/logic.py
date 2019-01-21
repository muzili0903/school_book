# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-21 下午2:42
@Author  : muzili
@File    : logic
'''
import time
import uuid

import requests
from django.core.cache import cache

from common.verify_code import gen_verify_code
from book import yzx_config
from user.models import User


def check_code(phone, vcode):
    key = '%s-verify_code' % phone
    code = cache.get(key)
    return vcode == code


def check_password(password, psd):
    return password == psd


def check_username(username):
    return True


def create_user(phone, username, password):
    t = str(time.time())
    u = str(uuid.uuid4())
    uid = u + t
    User.objects.create(u_id=uid, u_phone=phone, u_name=username, u_password=password)
    return {'msg': 'register success'}


def verify_code(phone):
    code = gen_verify_code()
    print(code, '-------------------->')
    key = '%s-verify_code' % phone
    cache.set(key, code)
    sms_cfg = yzx_config.HY_SMS_PARAMS.copy()
    sms_cfg['mobile'] = phone
    sms_cfg['param'] = sms_cfg['param'] % (code, 60)
    requests.post(yzx_config.HY_SMS_URL)
    return {'msg': 'message send success'}


def verify_msg(phone, username, password, psd, vcode):
    vcode = check_code(phone, vcode)
    vpassword = check_password(password, psd)
    vusername = check_username(username)
    if vcode and vpassword and vusername:
        return create_user(phone, username, password)
    else:
        return {'msg': 'register fail'}


def verify_login(username, password):
    user = User.objects.get(u_name=username)
    if user:
        if check_password(password, user.u_password):
            return user
    return None
