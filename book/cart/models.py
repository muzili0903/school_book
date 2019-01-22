from django.db import models


# Create your models here.
class Cart(models.Model):
    u_id = models.CharField(max_length=128)
    g_id = models.CharField(max_length=128)
    c_num = models.IntegerField()
    c_total_price = models.FloatField()
    c_is_delete = models.BooleanField(default=0)

    def to_dict(self):
        return {
            'uid': self.u_id,
            'gid': self.g_id,
            'c_total_price': self.c_total_price
        }
