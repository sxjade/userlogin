from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    usergroup = models.CharField(max_length=30)
    reserve = models.CharField(max_length=30)
    validity = models.DateTimeField()
    
    class Meta:
        unique_together = ('username','usergroup')
        
    primary = ('username','usergroup')
    
    def __unicode__(self):
        return '%s,%s'%(self.username,self.usergroup)
    
    
class Login_log(models.Model):
    username = models.CharField(max_length=30)
    login_time = models.DateTimeField()
    

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

