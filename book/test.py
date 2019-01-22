# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-21 下午3:49
@Author  : muzili
@File    : test
'''
from datetime import datetime
now = datetime.now()
tim = now.strftime('%Y-%m-%d %H:%M:%S')
print(tim)
print(type(tim))
