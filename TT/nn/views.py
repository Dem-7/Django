from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def rr(request):
    return HttpResponse("<h1>Первая страница моего  сайта на  Django</h1>")

def ll(request):
    return HttpResponse("<h1>Вторая страница моего  сайта на  Django</h1>")