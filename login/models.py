# -*- coding:utf-8 -*-
from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    groupname = models.CharField(max_length=30)
    reserve = models.CharField(max_length=30)
    validity = models.DateTimeField()
    
    class Meta:
        unique_together = ('username','groupname')
        
    primary = ('username','groupname')
    
    def __unicode__(self):
        return '%s,%s'%(self.username,self.groupname)
    
    
class Login_log(models.Model):
    username = models.CharField(max_length=30)
    login_time = models.DateTimeField()
    
    def __unicode__(self):
        return '%s' % self.username

class Login_fail_log(models.Model):
    username = models.CharField(max_length=30)
    groupname = models.CharField(max_length=30)
    reserve = models.CharField(max_length=30)
    reason = models.CharField(max_length=50)
    login_time = models.DateTimeField()

    def __unicode__(self):
        return '%s' % self.username

class Collect(models.Model):
    TerminalCompany = models.CharField(max_length=30, default='l')
    TerminalName = models.CharField(max_length=30, default='l')
    AccountCompany = models.CharField(max_length=30, default='l')
    AccountNumber = models.CharField(max_length=30, default='l')
    AccountCurrency = models.CharField(max_length=30, default='l')
    AccountLeverage = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    AccountBalance = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    AccountEquity = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    AccountMargin = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    AccountProfit = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    MarginReq = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    AccountFreeMargin = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    Spread = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    OrderCommission = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    AllAmount = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    Profit = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    HoldProfit = models.DecimalField(max_digits=30,decimal_places=4,default=0.00)
    updatetime = models.DateTimeField()
    
    def __unicode__(self):
        return '%s' % self.TerminalCompany


class Market(models.Model):
    username = models.CharField(max_length=30)
    groupname = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    updatetime = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('username','groupname')
        
    primary = ('username','groupname')
    
    def __unicode__(self):
        return '%s,%s'%(self.username,self.groupname)


