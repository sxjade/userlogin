# -*- coding:utf-8 -*-
'''
@author: liuyang
'''
from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^settrade',views.setTrade, name='trade'),
    url(r'^gettrade',views.getTrade, name='getTrade'),
               ]
