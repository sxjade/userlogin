# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import User, Login_log, Collect, Market, Login_fail_log
from django.http import HttpResponse
import json
from datetime import datetime,timedelta
from django.utils import timezone
from .pages import Page
from decimal import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return HttpResponse("login test")

def setlogin_error(username,groupname,reserve,reason,login_time):
    
    log_error = Login_fail_log(username=username,groupname=groupname,reserve=reserve,reason=reason,login_time=login_time)
    log_error.save()
    
    
def login(request):
    result = {}
    username = request.GET.get('username','')
    groupname = request.GET.get('groupname','')
    reserve = request.GET.get('reserve','')
    
    this_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    
    print(username,groupname)
    if(username==''):
        result['status'] = 'error'
        result['errmsg'] = 'empty username!'
        setlogin_error(username,groupname,reserve,result['errmsg'],this_time)
        return HttpResponse(json.dumps(result))
    
    try:
        user = User.objects.get(username=username,groupname=groupname)
        validity = user.validity
        valstr = datetime.strftime(validity,'%Y-%m-%d %H:%M:%S')
        result['validity'] = valstr 
    except User.DoesNotExist:
        result['status'] = 'error'
        result['errmsg'] = 'username or group not exist'
        setlogin_error(username,groupname,reserve,result['errmsg'],this_time)
        return HttpResponse(json.dumps(result))
    
    if(user.reserve == reserve):
          
        if this_time > validity:
            result['status'] = 'error'
            result['errmsg'] = 'Be validity'
            setlogin_error(username,groupname,reserve,result['errmsg'],this_time)
            return HttpResponse(json.dumps(result))
            
        result['status'] = 'ok'
            
        try:
            log = Login_log(username=username,login_time=this_time)
            log.save()   
        except Login_log.DoesNotExist:
            result['log'] = 'error'
            result['errmsg'] = 'log not exist'
            return HttpResponse(json.dumps(result))
            
        return HttpResponse(json.dumps(result))
    
    else:
        result['status'] = 'error'
        result['errmsg'] = 'reserve error'
        setlogin_error(username,groupname,reserve,result['errmsg'],this_time)
    
    
        
    return HttpResponse(json.dumps(result))

@login_required(login_url='/admin/')
def showlog(request):
    
#    if loginTrueOrF(request) == False:
#        return render(request,'admin/base_site.html')
    
    status = {}
    current_page = request.GET.get('page','1')
             
    all_item = Login_log.objects.filter(**status).count()
             
    page_obj = Page(current_page,status)
    log_list = Login_log.objects.filter(**status).order_by('-login_time')[page_obj.start():page_obj.end()]   # order_by('-updatetime')
             
    page_str,per_page,next_page,all_page,fir_page,end_page = page_obj.page_str(all_item, '/login/showlog')
    page_list = range(1,all_page+1)
    print page_str
    content = {'log_list':log_list,'page_str':page_str,'per_page':per_page,'next_page':next_page,'all_page':all_page,'page_list':page_list,'fir_page':fir_page,'end_page':end_page,'current_page':current_page}
             
    
    return render(request, 'login/templates/login_log.html', content)



def getCollect(request):
    result={}
    TerminalCompany = request.GET.get('TerminalCompany','1')
    TerminalName = request.GET.get('TerminalName','1')
    AccountCompany = request.GET.get('AccountCompany','1')
    AccountNumber = request.GET.get('AccountNumber','1')
    AccountCurrency = request.GET.get('AccountCurrency','1')
    
    AccountLeverage = Decimal(request.GET.get('AccountLeverage','1'))
    AccountBalance = Decimal(request.GET.get('AccountBalance','1'))
    AccountEquity = Decimal(request.GET.get('AccountEquity','1'))
    AccountMargin = Decimal(request.GET.get('AccountMargin','1'))
    AccountProfit = Decimal(request.GET.get('AccountProfit','1'))
    MarginReq = Decimal(request.GET.get('MarginReq','1'))
    AccountFreeMargin = Decimal(request.GET.get('AccountFreeMargin','1'))
    Spread = Decimal(request.GET.get('Spread','1'))
    OrderCommission = Decimal(request.GET.get('OrderCommission','1'))
    AllAmount = Decimal(request.GET.get('AllAmount','1'))
    Profit = Decimal(request.GET.get('Profit','1'))
    HoldProfit = Decimal(request.GET.get('HoldProfit','1'))
    
    this_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    try:
        cols=Collect(TerminalCompany=TerminalCompany,TerminalName=TerminalName,AccountCompany=AccountCompany, \
                        AccountNumber=AccountNumber,AccountCurrency=AccountCurrency, \
                AccountLeverage=AccountLeverage,AccountBalance=AccountBalance,AccountEquity=AccountEquity, \
                AccountMargin=AccountMargin,AccountProfit=AccountProfit, \
                MarginReq=MarginReq,AccountFreeMargin=AccountFreeMargin,Spread=Spread, \
                OrderCommission=OrderCommission,AllAmount=AllAmount,Profit=Profit, \
                HoldProfit=HoldProfit,updatetime=this_time
                )
        cols.save()
    except Collect.DoesNotExist:
        result['log'] = 'error'
        
        return HttpResponse(json.dumps(result))
    
    result['status'] = 'ok'
    return HttpResponse(json.dumps(result))

@login_required(login_url='/admin/')
def showCollect(request):
    
    status = {}
    current_page = request.GET.get('page','1')
             
    all_item = Collect.objects.filter(**status).count()
             
    page_obj = Page(current_page,status)
    collect_list = Collect.objects.filter(**status).order_by('-updatetime')[page_obj.start():page_obj.end()]   # order_by('-updatetime')
             
    page_str,per_page,next_page,all_page,fir_page,end_page = page_obj.page_str(all_item, '/login/showcollect')
    page_list = range(1,all_page+1)
    print page_str
    content = {'collect_list':collect_list,'page_str':page_str,'per_page':per_page,'next_page':next_page,'all_page':all_page,'page_list':page_list,'fir_page':fir_page,'end_page':end_page,'current_page':current_page}
             
    
    return render(request, 'login/templates/get_Collect.html', content)


def getMarket(request):
    result = {}
    username = request.GET.get('username','')
    groupname = request.GET.get('groupname','')
    content = request.GET.get('content','')
    this_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    print(username,groupname)
    if(username==''):
        result['status'] = 'error'
        result['errmsg'] = 'empty username!'
        return HttpResponse(json.dumps(result))
    
    try:
        market = Market.objects.get(username=username,groupname=groupname)
        if market:
            market.content = content
            market.updatetime = this_time
            market.save()
            result['status'] = 'ok'
            return HttpResponse(json.dumps(result))
        
            
    except Market.DoesNotExist:
        try:
            market = Market(username=username,groupname=groupname,content=content,updatetime = this_time)
            market.save()
            result['status'] = 'ok'
            return HttpResponse(json.dumps(result))
        except Market.DoesNotExist:
            result['status'] = 'error'
        
            return HttpResponse(json.dumps(result))
        
        
@login_required(login_url='/admin/')
def showMarket(request):
    status = {}
    current_page = request.GET.get('page','1')
             
    all_item = Market.objects.filter(**status).count()
             
    page_obj = Page(current_page,status)
    market_list = Market.objects.filter(**status).order_by('-updatetime')[page_obj.start():page_obj.end()]   # order_by('-updatetime')
             
    page_str,per_page,next_page,all_page,fir_page,end_page = page_obj.page_str(all_item, '/login/showMarket')
    page_list = range(1,all_page+1)
    print page_str
    content = {'market_list':market_list,'page_str':page_str,'per_page':per_page,'next_page':next_page,'all_page':all_page,'page_list':page_list,'fir_page':fir_page,'end_page':end_page,'current_page':current_page}
             
    
    return render(request, 'login/templates/get_market.html', content)



