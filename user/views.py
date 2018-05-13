# encoding: utf-8
from django.shortcuts import render

from django.http import HttpResponse
from .models import get_users, valid_login_model
import time


def index(request):
    return render(request, 'user/index.html', {
        'users': get_users()
    })


def login(request):
    return render(request, 'user/login.html')


def valid_login(request):
    name = '刘伟'
    password = '123'

    login_user = valid_login_model(name, password);
    if login_user:
        return render(request, 'user/index.html', {
            'users': get_users(),
            'login_user': login_user
        })
    else:
        return render(request, 'user/login.html', {'error_message': 'Login Fail! Name or password is not correct!'})


def user_add(request):
    return render(request, 'user/user_add.html')

# Create your views here.
