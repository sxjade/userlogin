# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import Tradelist
from django.http import HttpResponse
import json
import datetime
from datetime import timedelta
from django.utils import timezone
# Create your views here.


def setTrade(request):
    result = {}
    codename = request.GET.get('codename','1')
    bos = int(request.GET.get('bos','1'))
    oorc = int(request.GET.get('oorc','1'))
    vol = int(request.GET.get('vol','1'))
    price = float(request.GET.get('price','1'))
    
    this_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc)
    try:
        trade=Tradelist(codename=codename,bos=bos,oorc=oorc, vol=vol,price=price, updatetime=this_time)
        trade.save()
    except Tradelist.DoesNotExist:
        result['log'] = 'error'
        
        return HttpResponse(json.dumps(result))
    
    result['status'] = 'ok'
    return HttpResponse(json.dumps(result))
    
 
def getTrade(request):
    result = {}
    codename = request.GET.get('codename','1')
    min = int(request.GET.get('min','0'))
    max_id = int(request.GET.get('id','0'))
    
    today = datetime.date.today()
    this_time = datetime.datetime.utcnow().replace(tzinfo=timezone.utc)
    if min == 0:
        start_time = today
    else:
        start_time = this_time - datetime.timedelta( mins = min )
    
    try:
        if codename != '1':
            trade_list = Tradelist.objects.filter(updatetime__range=(start_time,this_time), id__gt = max_id, codename=codename).order_by('-updatetime') 
        else:
            trade_list = Tradelist.objects.filter(updatetime__range=(start_time,this_time), id__gt = max_id,).order_by('-updatetime')
            
    except Tradelist.DoesNotExist:
        result['log'] = 'error'
        return HttpResponse(json.dumps(result))
    
    tra_list_dict = trade2str(trade_list)
    result['allList'] = tra_list_dict
    return HttpResponse(json.dumps(result))
    
 
def trade2str(trlist):
    tra_dict = {}
    tra_list = []
    if trlist:
        for tra in trlist:
            if tra:
                tra_dict['codename'] = tra.getname()
                tra_dict['bos'] = tra.getbos()
                tra_dict['oorc'] = tra.getoorc()
                tra_dict['vol'] = tra.getvol()
                tra_dict['price'] = tra.getprice()
                tra_dict['updatetime'] = tra.gettime()
                tra_list.append(tra_dict)
    
    return tra_list
            
    