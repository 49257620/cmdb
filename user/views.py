# encoding: utf-8
from django.shortcuts import render,redirect

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
    name = request.GET.get('name')
    password = request.GET.get('password')

    login_user = valid_login_model(name, password)
    if login_user:
        """
        return render(request, 'user/index.html', {
            'users': get_users(),
            'login_user': login_user
        })
        return redirect("user:index")
        return redirect("/user/index/")
        """
        return redirect("user:index")
    else:
        return render(request, 'user/login.html', {
            'error_message': 'Login Fail! Name or password is not correct!',
            'name': name
        })


def user_add(request):
    return render(request, 'user/user_add.html')

# Create your views here.
