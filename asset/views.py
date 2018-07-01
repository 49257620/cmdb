from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Host


# Create your views here.


def index(request):
    return render(request, 'asset/index.html')


def list_ajax(request):
    result = [host.as_dict() for host in Host.objects.all()]
    return JsonResponse({"code": 200, "result": result})
