
from django.http import HttpResponse
from django.shortcuts import render


def ddt(request):
    ff = {"asd":"нашего сайта"}
    return render(request, 'nn/index.html' , ff)

def ddd(request):
    ff = {'asd': "нашего сайта"}
    return render(request , 'nn/kort.html' , ff)

def lll(request):
    return  HttpResponse("<h1>Это третья страница моего сайта на Django</h1>")
