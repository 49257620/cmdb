# encoding: utf-8
"""
-- 生成migrate sql 创建前移文件
python manage.py makemigrations

-- 执行migrate sql
python manage.py migrate user

-- 查看migrate sql
"""
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32, null=False, default='')
    password = models.CharField(max_length=32, null=False, default='')
    age = models.IntegerField(null=False, default=0)
    tel = models.CharField(max_length=32, null=False, default='')
    sex = models.BooleanField(null=False, default=True)
    addr = models.CharField(max_length=512, null=False, default='')
    remark = models.CharField(max_length=512, null=False, default='')
    create_time = models.DateTimeField(null=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'sex': self.sex,
            'age': self.age,
            'tel': self.tel,
            'remark': self.remark
        }

