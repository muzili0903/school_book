from django.db import models

# Create your models here.
from cart.models import CartHistory
from user.models import Profile


class Order(models.Model):
    '''
    订单状态：
    1--->生成订单，未付款
    2--->付款待收货
    3--->收货待评价
    4--->已评价
    '''
    o_id = models.CharField(max_length=128, unique=True, verbose_name='订单号')
    u_id = models.CharField(max_length=128, verbose_name='买家ID')
    o_date = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    o_message = models.CharField(max_length=128, verbose_name='留言')
    o_total_price = models.FloatField(verbose_name='总价')
    o_status = models.IntegerField(verbose_name='订单状态')
    o_is_delete = models.BooleanField(default=False, verbose_name='是否删除订单')

    def to_dict(self):
        cart = CartHistory.mark(self.u_id, self.o_id)
        return {
            'oid': self.o_id,
            'goods': cart['good'],
            'date': self.o_date.strftime('%Y-%m-%d %H:%M:%S'),
            'message': self.o_message,
            'total_price': self.o_total_price,
            'user': Profile.search(self.u_id),
            'status': self.o_status
        }
