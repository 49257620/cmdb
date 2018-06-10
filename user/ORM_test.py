# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from user.models import User
from datetime import datetime

for i in range(10):
    u = User()
    u.name = 'kk_{0}'.format(i)
    u.age = i + 1
    u.create_time = datetime.now()
    u.save()

# <
User.objects.filter(age__lt=5)
# <=
User.objects.filter(age__lte=5)
# >
User.objects.filter(age__gt=5)
# >=
User.objects.filter(age__gte=5)
# like %%
User.objects.filter(name__contains='kk')
# like %val
User.objects.filter(name__startswith='kk')
# like val%
User.objects.filter(name__endswith='9')
# and
User.objects.filter(age__gt=5, name__endswith='9')
# in
User.objects.filter(age__in=[4, 5])
# count with conditions
User.objects.exclude(age=9).count()


# 排序
User.objects.all().order_by('id')
# 倒叙
User.objects.all().order_by('-id')
# 多排序
User.objects.all().order_by('-id', 'age')


# 批量更新
User.objects.filter(age__gt=8).update(age=20,addr='上海')

