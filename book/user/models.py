from django.db import models


# Create your models here.
class User(models.Model):
    '''用户模块'''
    u_id = models.CharField(max_length=128, unique=True)
    u_name = models.CharField(max_length=64, verbose_name='用户名')
    u_phone = models.CharField(max_length=32, verbose_name='手机号')
    u_password = models.CharField(max_length=128, verbose_name='密码')
