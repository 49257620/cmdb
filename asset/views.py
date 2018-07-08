from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Host,Resource
from django.utils import timezone
from datetime import timedelta


# Create your views here.


def index(request):
    return render(request, 'asset/index.html')


def list_ajax(request):
    result = [host.as_dict() for host in Host.objects.all()]
    return JsonResponse({"code": 200, "result": result})


def monitor_ajax(request):
    ip = request.GET.get('ip')
    xAxis = []
    CPU_data = []
    MEM_data = []
    start_time = timezone.now() - timedelta(days=1)
    print(ip)
    resources = Resource.objects.filter(collect_time__gte=start_time,ip=ip).order_by('collect_time')
    for r in resources:
        xAxis.append(r.collect_time.strftime('%Y-%m-%d %H:%M'))
        CPU_data.append(r.cpu)
        MEM_data.append(r.mem)
    return JsonResponse({"code": 200, "result": {'xAxis':xAxis,'cpu':CPU_data,'mem':MEM_data}})
