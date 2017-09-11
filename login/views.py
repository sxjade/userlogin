from django.shortcuts import render
from models import User,Login_log
from django.http import HttpResponse
import json
from datetime import datetime,timedelta
from django.utils import timezone
from .pages import Page
# Create your views here.

def index(request):
    return HttpResponse("login test")

def loginTrueOrF(request):
    try:
        if request.session['username']:
            return True
    except:
        return False
    
def login(request):
    result = {}
    username = request.GET.get('username','')
    usergroup = request.GET.get('usergroup','')
    reserve = request.GET.get('reserve','')
    print(username,usergroup)
    if(username==''):
        result['status'] = 'error'
        result['errmsg'] = 'empty username!'
        return HttpResponse(json.dumps(result))
    
    try:
        user = User.objects.get(username=username,usergroup=usergroup)
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
