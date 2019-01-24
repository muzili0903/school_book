from django.contrib import admin

# Register your models here.
from books.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    search_fields = ['g_stock', 'g_sale', 'g_price']
    # list_editable = ['g_stock', 'g_price']
    list_per_page = 50
    list_filter = ['u_id']



admin.site.register(Goods, GoodsAdmin)
