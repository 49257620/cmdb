# encoding: utf-8
import json
from django.db import models

# Create your models here.

DATA_FILE = 'user.data.txt'


def get_users():
    f_handler = open(DATA_FILE, 'rt', encoding='utf-8')
    users = json.loads(f_handler.read())
    f_handler.close()
    return users


def valid_login_model(name,password):
    users = get_users()
    user_login = None
    for uid, user in users.items():
        if user['name'] == name and user['password'] == password:
            user_login = user
            break
    return user_login
