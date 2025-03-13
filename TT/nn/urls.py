from django.urls import path
from . import views


urlpatterns = [
    path ('' , views.ddt ) ,
    path ('data' , views.ddd) ,
    path ('test' ,views.lll)
]