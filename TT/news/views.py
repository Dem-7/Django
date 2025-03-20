from django.shortcuts import render
from .models import Novost

# Create your views here.
def jjj(request):
    dd = Novost.objects.all()
    a = {"f": "страница" ,"k":dd}
    return render(request , 'news/novosti.html' , a)

