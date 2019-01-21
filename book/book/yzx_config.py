# -*- coding:utf-8 -*-
'''
@project : book
@Time    : 19-1-21 下午3:14
@Author  : muzili
@File    : yzx_config
'''
# HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
# HY_SMS_PARAMS = {
#     'account': 'C42331298',
#     'password': '2d2284b74dc4972da3df3915fb17b28f',
#     'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
#     'mobile': None,
#     'format': 'json',
# }

import requests

HY_SMS_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
HY_SMS_PARAMS = {
    "sid": "a2dbe2f942268d00abc071938a8ec263",
    "token": "fe488d6a51aca562800a3cc9440deb86",
    "appid": "3f3267c831e94f94baf4530d490decd4",
    "templateid": "403022",
    "param": "%s,%s",
    "mobile": 15889926155,
    "uid": "2d92c6132139467b989d087c84a365d8"
}
response = requests.post(url=HY_SMS_URL, data=HY_SMS_PARAMS)
print(response.text)