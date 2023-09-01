from urllib import request

from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    path('', views.demo1, name='demo1'),

    #  path('home/',views.home,name='home'),
  #  path('contact/',views.contact,name='contact'),
   # path('thanks/',views.thanks,name='thanks'),
    #path('detail/',views.detail,name='detail'),
    #path('add/',views.addition,name='addition'),




]
