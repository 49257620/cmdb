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
