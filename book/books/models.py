import random

from django.db import models


# Create your models here.
class Goods(models.Model):
    g_id = models.CharField(max_length=128, verbose_name='书本ID')
    u_id = models.CharField(max_length=128, verbose_name='卖家ID')
    # 评论id可能用不到
    g_c_id = models.CharField(max_length=128, verbose_name='评论ID')
    g_name = models.CharField(max_length=64, verbose_name='书名')
    g_price = models.FloatField(verbose_name='价格')
    g_stock = models.IntegerField(verbose_name='库存')
    g_image = models.CharField(max_length=128, verbose_name='图片')
    g_author = models.CharField(max_length=128, verbose_name='作者')
    g_sale = models.IntegerField(verbose_name='销量')
    g_type = models.IntegerField(verbose_name='类型')

    def to_dict(self):
        return {
            'comment': [comment.to_dict() for comment in Comment.objects.filter(g_id=self.g_id)],
            'g_name': self.g_name,
            'g_author': self.g_author,
            'g_price': self.g_price,
            'g_stock': self.g_stock,
            'g_sale': self.g_sale,
            'g_image': self.g_image,
            'g_type': self.g_type,
        }


class Comment(models.Model):
    u_id = models.CharField(max_length=128, verbose_name='买家ID')
    g_id = models.CharField(max_length=128, verbose_name='商品ID')
    comment = models.CharField(max_length=256, verbose_name='评价')
    com_data = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'uid': self.u_id,
            'comment': self.comment,
            'com_data': self.com_data,
        }
