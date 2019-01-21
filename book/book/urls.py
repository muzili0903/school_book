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

from books.api import best_seller, computer_book, life_book, success_book, sale_descending_order, sort_type_book
from books.api import price_descending_order, price_ascending_order
from user.api import register, send_verify_code, phone_login, user_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/user/register/$', register),
    url(r'^api/user/verify_code/$', send_verify_code),
    url(r'^api/user/phone_login/$', phone_login),
    url(r'^api/user/user_login/$', user_login),

    url(r'^api/books/best_seller/$', best_seller),
    url(r'^api/books/computer_book/$', computer_book),
    url(r'^api/books/life_book/$', life_book),
    url(r'^api/books/success_book/$', success_book),
    url(r'^api/books/price_descending_order/$', price_descending_order),
    url(r'^api/books/price_ascending_order/$', price_ascending_order),
    url(r'^api/books/sale_descending_order/$', sale_descending_order),
    url(r'^api/books/sort_type_book/$', sort_type_book),
]
