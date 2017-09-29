# -*- coding:utf-8 -*-
'''
@author: liuyang
'''
from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^index',views.index, name='index'),
    url(r'^userlogin',views.login, name='login'), 
    url(r'^showlog',views.showlog, name='showlog'), 
    url(r'^collect',views.getCollect, name='collect'), 
    url(r'^showcollect',views.showCollect, name='showcollect'), 
    url(r'^market',views.getMarket, name='market'), 
    url(r'^showMarket',views.showMarket, name='showMarket'), 
    url(r'^admin/', include(admin.site.urls)),
    
               ]
