# encoding: utf-8
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import get_users, valid_login_model,valid_create_user,create_user,get_user,valid_update_user,update_user,delete_user,user_change_pwd_chk,update_user_password
import time


def index(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    return render(request, 'user/index.html', {
        'users': get_users()
    })


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')

        login_user = valid_login_model(name, password)
        if login_user:
            request.session['login_user'] = login_user
            return redirect("user:index")
        else:
            return render(request, 'user/login.html', {
                'error_message': 'Login Fail! Name or password is not correct!',
                'name': name
            })


def valid_login(request):
    name = request.POST.get('name')
    password = request.POST.get('password')

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


def logout(request):
    request.session.flush()
    return redirect("user:login")


def user_add(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        return render(request, 'user/user_add.html')
        # return redirect('user:user_add')
    else:
        is_valid, user, errors = valid_create_user(request.POST)
        if is_valid:
            create_user(user)
            return redirect('user:index')
        else:
            return render(request, 'user/user_add.html', {
                'user': user,
                'errors': errors,
            })


def user_update(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        uid = request.GET.get('uid', '')

        return render(request, 'user/user_update.html',{
            'user' : get_user(uid)
        })
        # return redirect('user:user_add')
    else:
        is_valid, user, errors = valid_update_user(request.POST)
        if is_valid:
            update_user(user)
            return redirect('user:index')
        else:
            user['id'] = request.POST.get('id','')
            return render(request, 'user/user_update.html', {
                'user': user,
                'errors': errors,
            })


def user_delete(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        return redirect('user:index')
    else:
        del_users = request.POST.getlist('del_users[]', '')
        for uid in del_users:
            delete_user(uid)
        return redirect('user:index')


def user_chpwd(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        return render(request, 'user/user_chpwd.html' )
    else:
        is_valid,pwd, errors = user_change_pwd_chk(request)
        if is_valid:

            login_user['password'] = pwd
            update_user_password(login_user)
            request.session['login_user'] = login_user
            return redirect('user:index')
        else:
            return render(request, 'user/user_chpwd.html', {
                'errors': errors,
            })