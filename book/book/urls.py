"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from user.api import register, send_verify_code, phone_login, user_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/user/register/$', register),
    url(r'^api/user/verify_code/$', send_verify_code),
    url(r'^api/user/phone_login/$', phone_login),
    url(r'^api/user/user_login/$', user_login),
]
