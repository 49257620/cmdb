# encoding: utf-8
from django.shortcuts import render, redirect

from django.http import HttpResponse,JsonResponse
# from .modelsv3 import get_users, valid_login_model,valid_create_user,create_user,get_user,valid_update_user,update_user,delete_user,user_change_pwd_chk,update_user_password,search_users
import time

from .models import User
from .UserValidator import UserValidator


def index(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        return render(request, 'user/index.html', {
            'users': User.objects.all()
        })
    else:
        conditions = request.POST.get('search_condition', '')
        return render(request, 'user/index.html', {
            'users': User.objects.filter(name__contains=conditions)
        })


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')

        login_user = UserValidator.login_valid(name, password)
        if login_user:
            request.session['login_user'] = login_user.as_dict()
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
        is_valid, user, errors = UserValidator.valid_create_user(request.POST)
        if is_valid:
            user.save()
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
            'user' : User.objects.get(id=uid)
        })
        # return redirect('user:user_add')
    else:
        is_valid, user, errors = UserValidator.valid_update_user(request.POST)
        if is_valid:
            user.save()
            return redirect('user:index')
        else:
            #user['id'] = request.POST.get('id','')
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
            User.objects.get(id=uid).delete()
        return redirect('user:index')


def user_chpwd(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        return render(request, 'user/user_chpwd.html' )
    else:
        is_valid,pwd, errors = UserValidator.user_change_pwd_chk(request)
        if is_valid:

            login_user['password'] = pwd
            user = User.objects.get(id=login_user['id'])
            user.password = pwd
            user.save()
            request.session['login_user'] = login_user
            return redirect('user:index')
        else:
            return render(request, 'user/user_chpwd.html', {
                'errors': errors,
            })


def user_search(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return redirect('user:login')
    if request.method == 'GET':
        return redirect('user:index')
    else:
        conditions = request.POST.get('search_condition', '')
        return render(request, 'user/index.html', {
            'users': User.objects.filter(name__contains=conditions)
        })


def user_add_ajax(request):
    login_user = request.session.get('login_user')
    if not login_user:
        return JsonResponse({
            'code': 403,
            'message' : '未登陆',
            'result' : {}
        })

    is_valid, user, errors = UserValidator.valid_create_user(request.POST)
    if is_valid:
        user.save()
        return JsonResponse({
            'code': 200,
            'message': '保存成功',
            'result': user.as_dict()
        })
    else:
        return JsonResponse({
            'code': 400,
            'message': '数据错误',
            'result': errors
        })
