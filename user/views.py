# encoding: utf-8
from django.shortcuts import render

from django.http import HttpResponse
from .models import get_users
import time


def index(request):
    return render(request, 'user/index.html', {
        'users': get_users()
    })


def login(request):
    return render(request, 'user/login.html')


def user_add(request):
    return render(request, 'user/user_add.html')

# Create your views here.
