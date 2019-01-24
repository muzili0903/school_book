from django.db import models


# Create your models here.
class User(models.Model):
    '''用户模块'''
    u_id = models.CharField(max_length=128, unique=True)
    u_name = models.CharField(max_length=64, verbose_name='用户名')
    u_phone = models.CharField(max_length=32, verbose_name='手机号')
    u_password = models.CharField(max_length=128, verbose_name='密码')

    def to_dict(self):
        return {
            'u_name': self.u_name,
            'u_phone': self.u_phone,
            'profile': self.profile
        }

    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile, _ = Profile.objects.get_or_create(u_id=self.u_id)
        return self._profile


class Profile(models.Model):
    u_id = models.CharField(max_length=128)
    p_name = models.CharField(max_length=64)
    p_address = models.CharField(max_length=256)
    p_phone = models.CharField(max_length=32)

    def to_dict(self):
        return {
            'name': self.p_name,
            'address': self.p_address,
            'phone': self.p_phone
        }

    @classmethod
    def search(cls, uid):
        u_p = cls.objects.filter(u_id=uid).first()
        return u_p.to_dict()
