# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


class ViewClient(View):

    def get(self, request, *args, **kwargs):
        print(request.GET)
        print(request.POST)
        print(request.body)
        return HttpResponse('get ok')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ViewClient, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.GET)
        print(request.POST)
        print(request.body)
        return HttpResponse('post ok')
