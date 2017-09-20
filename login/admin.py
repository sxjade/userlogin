from django.contrib import admin
from .models import User, Collect, Login_log
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ['username','groupname','reserve','validity']

class Login_logAdmin(admin.ModelAdmin):
    list_display = ('username','login_time')
    
class CollectAdmin(admin.ModelAdmin):
    list_display = ('TerminalCompany','TerminalName','AccountCompany','AccountNumber','AccountCurrency','AccountLeverage',\
              'AccountBalance','AccountEquity','AccountMargin','AccountProfit','MarginReq','AccountFreeMargin', \
              'Spread','OrderCommission','AllAmount','Profit','HoldProfit','updatetime')
    
admin.site.register(User,UserAdmin)
admin.site.register(Collect,CollectAdmin)
admin.site.register(Login_log,Login_logAdmin)
