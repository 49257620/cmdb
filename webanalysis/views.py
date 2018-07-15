from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
import time
from .models import AccessLogFile,AccessLog
import json


# Create your views here.

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
