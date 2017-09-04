from django.shortcuts import render
from models import User,Login_log
from django.http import HttpResponse
import json
from datetime import datetime,timedelta
from django.utils import timezone
# Create your views here.

def index(request):
    return HttpResponse("login test")
    
def login(request):
    result = {}
    username = request.GET.get('username','')
    group = request.GET.get('group','')
    reserve = request.GET.get('reserve','')
    print(username,group)
    if(username==''):
        result['status'] = 'error'
        result['errmsg'] = 'empty username'
        return HttpResponse(json.dumps(result))
    
    try:
        user = User.objects.get(username=username,group=group)
    except User.DoesNotExist:
        result['status'] = 'error'
        result['errmsg'] = 'username or group not exist'
        return HttpResponse(json.dumps(result))
    
    if(user.reserve == reserve):
        validity = user.validity
            
        this_time = datetime.utcnow().replace(tzinfo=timezone.utc)
        print(validity,this_time)
            
        if this_time > validity:
            result['status'] = 'error'
            result['errmsg'] = 'Be validity'
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
        
    return HttpResponse(json.dumps(result))


