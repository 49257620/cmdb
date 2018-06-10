# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
from .models import User
from django.utils import timezone


class UserValidator(object):

    @staticmethod
    def login_valid(name, password):
        user = None
        try:
            user = User.objects.get(name=name)
        except BaseException as e:
            print(e)
            pass
        if user.password != password:
            user = None
        # print(result)
        return user

    @staticmethod
    def valid_create_user(post_info):
        add_user = User(name=post_info.get('name', '').strip(), password=post_info.get('password', '').strip(),
                        sex=post_info.get('sex', '').strip(), age=post_info.get('age', '').strip(),
                        tel=post_info.get('tel', '').strip(),
                        remark=post_info.get('remark', '').strip())
        password_confirm = post_info.get('password_confirm', '')

        is_valid = True
        errors = {}

        if add_user.name == '':
            is_valid = False
            errors['name'] = '用户名不能为空'
        else:
            print(add_user.name)
            try:
                result = User.objects.filter(name=add_user.name).exclude(age=0)
            except BaseException as e:
                print(e)
            print(result)
            if len(result) > 0:
                errors['name'] = '用户名已存在'
                is_valid = False

        if not add_user.age.isdigit():
            errors['age'] = '年龄格式错误'
            is_valid = False

        if add_user.password == '' or password_confirm != add_user.password:
            is_valid = False
            errors['password'] = '密码不能为空, 且两次输入密码必须相同'

        add_user.create_time = timezone.now()

        return is_valid, add_user, errors

    @staticmethod
    def valid_update_user(params):
        update_user = User(id=params.get('id', '').strip(), name=params.get('name', '').strip(),
                           password=params.get('password', '').strip(),
                           sex=params.get('sex', '').strip(), age=params.get('age', '').strip(),
                           tel=params.get('tel', '').strip(),
                           remark=params.get('remark', '').strip())
        is_valid = True
        errors = {}
        user_tmp = User.objects.get(id=update_user.id)

        if user_tmp is None:
            errors['id'] = '用户信息不存在'
            is_valid = False

        result = User.objects.filter(name=update_user.name).exclude(id=update_user.id)

        if len(result) > 0:
            errors['name'] = '用户名已存在'
            is_valid = False

        if not update_user.age.isdigit():
            errors['age'] = '年龄格式错误'
            is_valid = False

        user_tmp.name = update_user.name
        user_tmp.age = update_user.age
        user_tmp.tel = update_user.tel
        user_tmp.remark = update_user.remark
        user_tmp.sex = update_user.sex

        if is_valid:
            return is_valid, user_tmp, errors
        else:
            return is_valid, update_user, errors

    @staticmethod
    def user_change_pwd_chk(params):
        old_pw = params.POST.get('password_old', '')
        new_pw = params.POST.get('password', '')
        new_pw_confirm = params.POST.get('password_confirm', '')
        login_user = params.session.get('login_user')
        is_valid = True
        errors = {}

        session_pwd = login_user['password']
        if old_pw != session_pwd:
            errors['0001'] = '原密码错误'
            is_valid = False
        if new_pw != new_pw_confirm:
            errors['0002'] = '两次输入密码不一致'
            is_valid = False

        return is_valid, new_pw, errors