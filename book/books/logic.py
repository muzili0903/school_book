# Create your views here.
from books.models import Goods


def search_book():
    books = Goods.objects.all().order_by('-g_sale')
    book_list = [book.to_dict() for book in books]
    return book_list


def search_computer_book():
    books = Goods.objects.filter(g_type=3109)[0:10]
    book_list = [book.to_dict() for book in books]
    return book_list


def search_life_book():
    books = Goods.objects.filter(g_type=2199)[0:10]
    book_list = [book.to_dict() for book in books]
    return book_list


def search_success_book():
    books = Goods.objects.filter(g_type=2709)[0:10]
    book_list = [book.to_dict() for book in books]
    return book_list


def price_ascending():
    books = Goods.objects.all().order_by('g_price')[0:20]
    book_list = [book.to_dict() for book in books]
    return book_list


def price_descending():
    books = Goods.objects.all().order_by('-g_price')[0:20]
    book_list = [book.to_dict() for book in books]
    return book_list


def sale_descending():
    books = Goods.objects.all().order_by('-g_sale')[0:20]
    book_list = [book.to_dict() for book in books]
    return book_list


def sort_type(g_type):
    books = Goods.objects.filter(g_type=g_type)[0:20]
    book_list = [book.to_dict() for book in books]
    return book_list


def detail(gid):
    book = Goods.objects.filter(g_id=gid).first()
    return book.to_dict()
