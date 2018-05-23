# encoding: utf-8
import json
from django.db import models

# Create your models here.

DATA_FILE = 'user.data.dat'


def get_users():
    f_handler = open(DATA_FILE, 'rt', encoding='utf-8')
    users = json.loads(f_handler.read())
    f_handler.close()
    return users

def dump_users(users):
    fhandler = open(DATA_FILE, 'wt')
    fhandler.write(json.dumps(users))
    fhandler.close()
    return True

def valid_login_model(name,password):
    users = get_users()
    user_login = None
    for uid, user in users.items():
        if user['name'] == name and user['password'] == password:
            user['id'] = uid
            user_login = user
            break
    return user_login


def valid_create_user(post_info):
    name = post_info.get('name', '')
    password = post_info.get('password', '')
    password_confirm = post_info.get('password_confirm', '')
    sex = post_info.get('sex', '')
    age = post_info.get('age', '')
    tel = post_info.get('tel', '')
    desc = post_info.get('desc', '')

    is_valid = True
    user = {}
    errors = {}
    users = get_users()

    user['name'] = name.strip()

    if user['name'] == '':
        is_valid = False
        errors['name'] = '用户名不能为空'
    else:
        for uid, cuser in users.items():
            if cuser['name'] == user['name']:
                errors['name'] = '用户名已存在'
                is_valid = False
                break

    user['age'] = age.strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = tel
    user['sex'] = sex
    user['password'] = password.strip()
    user['desc'] = desc

    if user['password'] == '' or password_confirm != user['password']:
        is_valid = False
        errors['password'] = '密码不能为空, 且两次输入密码必须相同'

    return is_valid, user, errors


def create_user(params):
    users = get_users()
    uids = [int(key) for key in users]
    uid = max(uids + [0]) + 1
    users[uid] = params
    return dump_users(users)


def get_user(uid):
    users = get_users()
    user = users.get(uid, {})
    user['id'] = uid
    return user


def valid_update_user(params):
    uid = params.get('id', '')
    name = params.get('name', '')
    tel = params.get('tel', '')
    age = params.get('age', '')
    sex = params.get('sex', '')
    desc = params.get('desc','')
    print(uid)
    is_valid = True
    user = {}
    errors = {}
    users = get_users()

    user['id'] = uid.strip()
    if users.get(user['id']) is None:
        errors['id'] = '用户信息不存在'
        is_valid = False

    user['name'] = name.strip()

    for uid, cuser in users.items():
        if cuser['name'] == user['name'] and uid != user['id']:
            errors['name'] = '用户名已存在'
            is_valid = False
            break

    user['age'] = age.strip()
    if not user['age'].isdigit():
        errors['age'] = '年龄格式错误'
        is_valid = False

    user['tel'] = tel
    user['sex'] = sex
    user['desc'] = desc

    return is_valid, user, errors


def update_user(params):
    uid = params.pop('id')
    users = get_users()
    users[uid].update(params)
    return dump_users(users)


def delete_user(uid):
    users = get_users()
    users.pop(uid, None)
    dump_users(users)
    return True


def user_change_pwd_chk(params):
    old_pw = params.POST.get('password_old','')
    new_pw = params.POST.get('password','')
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