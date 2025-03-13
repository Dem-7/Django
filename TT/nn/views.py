
from django.http import HttpResponse

def ddt(request):
    return HttpResponse("<h1> Это первая страница моего сайта на Django </h1>")

def ddd(request):
    return HttpResponse("<h1> Это вторая страница моего сайта на Django </h1>")

def lll(request):
    return  HttpResponse("<h1>Это третья страница моего сайта на Django</h1>")
