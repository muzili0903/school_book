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
from user.models import User, Profile


def check_code(phone, vcode):
    key = '%s-verify_code' % phone
    code = cache.get(key)
    return vcode == code


def check_password(password, psd):
    return password == psd


def check_username(username):
    return True


def produce_id():
    t = str(time.time())
    u = str(uuid.uuid4())
    return u + t


def create_user(phone, username, password):
    uid = produce_id()
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


def set_profile(uid, address, phone, name):
    Profile.objects.update_or_create(u_id=uid, p_address=address, p_phone=phone, p_name=name)
    return {'msg': 'change success'}
