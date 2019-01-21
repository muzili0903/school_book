import random

from django.db import models


# Create your models here.
class Goods(models.Model):
    g_id = models.CharField(max_length=128, verbose_name='书本ID')
    u_id = models.CharField(max_length=128, verbose_name='卖家ID')
    g_c_id = models.CharField(max_length=128, verbose_name='评论ID')
    g_name = models.CharField(max_length=64, verbose_name='书名')
    g_price = models.FloatField(verbose_name='价格')
    g_stock = models.IntegerField(verbose_name='库存')
    g_image = models.CharField(max_length=128, verbose_name='图片')
    g_author = models.CharField(max_length=128, verbose_name='作者')
    g_sale = models.IntegerField(verbose_name='销量')
    g_type = models.IntegerField(verbose_name='类型')


class Comment(models.Model):
    u_id = models.CharField(max_length=128, verbose_name='买家ID')
    g_id = models.CharField(max_length=128, verbose_name='商品ID')
    comment = models.CharField(max_length=256, verbose_name='评价')
    com_data = models.DateTimeField(auto_now_add=True)
