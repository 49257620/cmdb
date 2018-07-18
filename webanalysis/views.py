from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
import time
from .models import AccessLogFile,AccessLog,AccessLogIps
import json
from functools import wraps


# Create your views here.

def login_chek(func):
    @wraps(func)
    def wrapper(request,*args,**kwargs):
        if request.session.get('login_user') is None:
            if request.is_ajax():
                return JsonResponse({
                    'code': 403,
                    'message' : '未登陆',
                    'result' : {}
                })
            return redirect("user:login")
        return func(request,*args,**kwargs)

    return wrapper

@login_chek
def index(request):
    files = AccessLogFile.objects.filter(status=0).order_by('-created_time')[:5]
    return render(request, 'webanalysis/index.html',{
            'files': files
        })


def upload(request):
    upload_file = request.FILES.get('log_file', None)
    # print(dir(upload_file))
    upload_path = os.path.join(settings.BASE_DIR, 'media', 'uploads', str(time.time()))
    with open(upload_path, 'wb') as fh:
        for chunk in upload_file.chunks():
            fh.write(chunk)
    log_file = AccessLogFile(name=upload_file.name, path=upload_path)
    log_file.save()
    notice_path = os.path.join(settings.BASE_DIR, 'media', 'notices', str(time.time()))
    with open(notice_path, 'w',encoding='utf-8') as fh:
        #print({'file_id': log_file.id, 'path': upload_path})
        fh.write(json.dumps({'file_id': log_file.id, 'path': upload_path}))
    return HttpResponse('upload ok')


def pie_data(request):
    print(request.GET.get('id'))
    legend,series = AccessLog.get_pie_data(AccessLog,id=request.GET.get('id'))

    return JsonResponse({"code":200,"result":{"legend":legend,"series":series}})

def bar_data(request):
    print(request.GET.get('id'))
    x,y = AccessLog.get_bar_data(AccessLog,id=request.GET.get('id'))

    return JsonResponse({"code":200,"result":{"x":x,"y":y}})


def sync_ips(request):
    AccessLogIps.syncIp()

    return JsonResponse({"code":200,"result":'同步成功'})


def map_data(request):
    print(request.GET.get('id'))
    x,y,z = AccessLog.get_map_data(AccessLog,id=request.GET.get('id'))

    return JsonResponse({"code":200,"result":{"x":x,"y":y,"z":z}})