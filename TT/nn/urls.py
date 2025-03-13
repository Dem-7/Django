from django.urls import path
from . import views


urlpatterns = [
    path ('' , views.ddt ) ,
    path ('vtoray' , views.ddd)
]