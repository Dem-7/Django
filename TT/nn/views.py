from django.shortcuts import render

# Create your views here.
def glavnay(request):
    a = {"f":"страница"}
    return render(request, 'nn/glavnay.html' , a)

def ttt(request):
    a = {"f": "страница"}
    return render(request, 'nn/kontakti.html', a)

def nnn(request):
    a = {"f": "страница"}
    return render(request , 'nn/onas.html' , a)