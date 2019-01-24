# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-24 上午10:13
@Author  : muzili
@File    : froms
'''
from django import forms

from user.models import Profile


class ProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'p_name', 'p_address', 'p_phone'
        ]
