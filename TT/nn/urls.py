from django.urls import path
from . import views


urlpatterns = [
    path ('' , views.ddt , name = 'odin' ) ,
    path ('data' , views.ddd , name = 'dva') ,
    path ('test' ,views.lll)
]