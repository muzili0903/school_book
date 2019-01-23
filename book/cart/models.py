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
            'num': self.c_num,
            'c_total_price': self.c_total_price
        }

    @classmethod
    def mark(cls, uid):
        carts = cls.objects.filter(u_id=uid, c_is_delete=1)
        goods = []
        total_price = 0
        for cart in carts:
            goods.append(cart.to_dict())
            total_price += cart.c_total_price
            cart.delete()
        return {'good': goods, 'total_price': total_price}


class CartHistory(models.Model):
    u_id = models.CharField(max_length=128)
    o_id = models.CharField(max_length=128)
    g_id = models.CharField(max_length=128)
    c_num = models.IntegerField()
    c_total_price = models.FloatField()

    def to_dict(self):
        return {
            'uid': self.u_id,
            'gid': self.g_id,
            'num': self.c_num,
            'c_total_price': self.c_total_price
        }

    @classmethod
    def mark(cls, uid, oid):
        carts = cls.objects.filter(u_id=uid, o_id=oid)
        goods = []
        total_price = 0
        for cart in carts:
            goods.append(cart.to_dict())
            total_price += cart.c_total_price
        return {'good': goods, 'total_price': total_price}
