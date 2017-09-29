# -*- coding:utf-8 -*-
from django.contrib import admin
from models import Tradelist
# Register your models here.

class TradelistAdmin(admin.ModelAdmin):
    fields = ['codename','bos','oorc','vol','price','updatetime']


admin.site.register(Tradelist,TradelistAdmin)


