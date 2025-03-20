from django.urls import path
from . import views


urlpatterns =[
    path('' ,views.glavnay  , name ='gl'),
    path('kontakti', views.ttt ,name ='ko'),
    path('onas' , views.nnn, name ='on')


]

#python manage.py runserver
