# -*- coding:utf-8 -*-
from django.db import models
import datetime
# Create your models here.

class Tradelist(models.Model):  # 成交列表表
    codename =  models.CharField(max_length=30)
    bos = models.IntegerField()     # 0:买    1:卖
    oorc = models.IntegerField()    # 0:开    1:平
    vol = models.IntegerField()     # 成交量
    price = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)    # 成交价格
    updatetime = models.DateTimeField()     # 成交时间
    
    def getname(self):
        return self.codename
    
    def getbos(self):
        return str(self.bos)
    
    def getoorc(self):
        return str(self.oorc)
    
    def getvol(self):
        return str(self.vol)
    
    def getprice(self):
        return str(self.price)
    
    def gettime(self):
        time1_str = datetime.datetime.strftime(self.updatetime,'%Y-%m-%d %H:%M:%S')
        return time1_str


