
# Create your views here.
from lib.http import render_json


def add_goods_cart(request):
    num = request.POST.get('num')
    g_id = request.POST.get('g_id')
    u_id = request.POST.get('u_id')
    result = add_goods(u_id, g_id, num)
    return render_json(result)



