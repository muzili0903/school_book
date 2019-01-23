# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-23 上午10:13
@Author  : muzili
@File    : middlerware
'''
from django.utils.deprecation import MiddlewareMixin

from common.defind_error import LOGIN_ERROR
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    WHITE_LIST = [
        '/api/user/register/',
        '/api/user/verify_code/',
        '/api/user/phone_login/',
        '/api/user/user_login/',

        '/api/books/best_seller/',
        '/api/books/computer_book/',
        '/api/books/life_book/',
        '/api/books/success_book/',
        '/api/books/price_descending_order/',
        '/api/books/price_ascending_order/',
        '/api/books/sale_descending_order/',
        '/api/books/sort_type_book/',
    ]

    def process_request(self, request):
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return

        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(u_id=uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None, code=LOGIN_ERROR)
