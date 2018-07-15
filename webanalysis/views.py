from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import time

# Create your views here.

def index(request):
    return render(request, 'webanalysis/index.html')


def upload(request):
    upload_file = request.FILES.get('log_file',None)
    #print(dir(upload_file))
    upload_path = os.path.join(settings.BASE_DIR,'media','uploads',str(time.time()))
    with open(upload_path,'wb') as fh:
        for chunk in upload_file.chunks():
            fh.write(chunk)
    return HttpResponse('upload ok')
