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

from books.api import best_seller, computer_book, life_book, success_book, sale_descending_order, sort_type_book, \
    book_detail
from books.api import price_descending_order, price_ascending_order
from cart.api import add_goods_cart, add_cart_num, reduce_cart_num, is_select_good, is_all_select_good, is_delete_cart
from mine.api import change_password, look_wait_payment, look_wait_goods, look_wait_comments, look_finish_comment, \
    look_finish_order
from order.api import order_status1, order_status2, order_status3, order_status4, delete_orders, delete_all_orders
from user.api import register, send_verify_code, phone_login, user_login, user_logout, user_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/user/register/$', register),
    url(r'^api/user/verify_code/$', send_verify_code),
    url(r'^api/user/phone_login/$', phone_login),
    url(r'^api/user/user_login/$', user_login),
    url(r'^api/user/user_logout/$', user_logout),
    url(r'^api/user/user_profile/$', user_profile),

    url(r'^api/books/best_seller/$', best_seller),
    url(r'^api/books/computer_book/$', computer_book),
    url(r'^api/books/life_book/$', life_book),
    url(r'^api/books/success_book/$', success_book),
    url(r'^api/books/price_descending_order/$', price_descending_order),
    url(r'^api/books/price_ascending_order/$', price_ascending_order),
    url(r'^api/books/sale_descending_order/$', sale_descending_order),
    url(r'^api/books/sort_type_book/$', sort_type_book),
    url(r'^api/books/book_detail/$', book_detail),

    url(r'^api/cart/add_goods_cart/$', add_goods_cart),
    url(r'^api/cart/add_cart_num/$', add_cart_num),
    url(r'^api/cart/reduce_cart_num/$', reduce_cart_num),
    url(r'^api/cart/is_select_good/$', is_select_good),
    url(r'^api/cart/is_all_select_good/$', is_all_select_good),
    url(r'^api/cart/is_delete_cart/$', is_delete_cart),

    url(r'^api/order/order_status1/$', order_status1),
    url(r'^api/order/order_status2/$', order_status2),
    url(r'^api/order/order_status3/$', order_status3),
    url(r'^api/order/order_status4/$', order_status4),
    url(r'^api/order/delete_orders/$', delete_orders),
    url(r'^api/order/delete_all_orders/$', delete_all_orders),

    url(r'^api/mine/change_password/$', change_password),
    url(r'^api/mine/look_wait_payment/$', look_wait_payment),
    url(r'^api/mine/look_wait_goods/$', look_wait_goods),
    url(r'^api/mine/look_wait_comments/$', look_wait_comments),
    url(r'^api/mine/look_finish_comment/$', look_finish_comment),
    url(r'^api/mine/look_finish_order/$', look_finish_order),
]
