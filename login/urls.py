# -*- coding:utf-8 -*-
'''
@author: liuyang
'''
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index',views.index, name='index'),
    url(r'^login',views.login, name='login'), 
    
               ]
