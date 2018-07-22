# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from asset.models import Host, Resource


class APIView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(APIView, self).dispatch(request, *args, **kwargs)

    def get_json(self):
        try:
            return json.loads(self.request.body)
        except BaseException as e:
            return {}

    def respones(self, result=None, code=200, errors={}):
        return JsonResponse({'code': code, 'result': result, 'errors': errors})


class ViewClient(APIView):

    def post(self, request, *args, **kwargs):
        print('is_ajax():',request.is_ajax())
        _ip = kwargs.get('ip', '')
        _json = self.get_json()

        ip = _ip
        name = _json.get('name', '')
        mac = _json.get('mac', '')
        os = _json.get('os', '')
        arch = _json.get('arch', '')
        mem = _json.get('mem', 0)
        cpu = _json.get('cpu', 0)
        disk = _json.get('disk', '{}')
        host = Host.create_or_replace(ip, name, mac, os, arch, mem, cpu, disk)

        return self.respones(host.as_dict())


class ViewResource(APIView):

    def post(self, request, *args, **kwargs):
        _ip = kwargs.get('ip', '')
        _json = self.get_json()

        record = Resource()
        record.ip = _ip
        record.cpu = _json.get('cpu', 0)
        record.mem = _json.get('mem', 0)
        record.save()

        return self.respones(record.as_dict())
