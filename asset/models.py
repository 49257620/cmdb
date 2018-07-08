from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone


class Host(models.Model):
    name = models.CharField(max_length=128, null=False, default='')
    ip = models.GenericIPAddressField(null=False, default='')
    mac = models.CharField(max_length=32, null=False, default='')
    os = models.CharField(max_length=64, null=False, default='')
    arch = models.CharField(max_length=16, null=False, default='')
    mem = models.BigIntegerField(null=False, default=0)
    cpu = models.IntegerField(null=False, default=0)
    disk = models.CharField(max_length=512, null=False, default='')

    sn = models.CharField(max_length=128, null=False, default='')
    user = models.CharField(max_length=128, null=False, default='')
    remark = models.TextField()
    purchase_time = models.DateTimeField(null=False)
    over_insurance_time = models.DateTimeField(null=False)

    created_time = models.DateTimeField(null=False, auto_now_add=True)
    last_time = models.DateTimeField(null=False)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ip': self.ip,
            'mac': self.mac,
            'os': self.os,
            'arch': self.arch,
            'mem': self.mem,
            'cpu': self.cpu,
            'disk': self.disk,
            'sn': self.sn,
            'user': self.user,
            'remark': self.remark,
            'purchase_time': self.purchase_time,
            'over_insurance_time': self.over_insurance_time,
            'created_time': self.created_time,
            'last_time': self.last_time
        }

    @classmethod
    def create_or_replace(cls, ip, name, mac, os, arch, mem, cpu, disk):
        host = None
        try:
            host = cls.objects.get(ip=ip)
        except ObjectDoesNotExist as e:
            host = cls()
            host.ip = ip
            host.purchase_time = timezone.now()
            host.over_insurance_time = timezone.now()

        host.name = name
        host.mac = mac
        host.os = os
        host.arch = arch
        host.mem = mem
        host.cpu = cpu
        host.disk = disk

        host.last_time = timezone.now()
        host.save()

        return host


class Resource(models.Model):
    ip = models.GenericIPAddressField(null=False, default='')
    cpu = models.FloatField(null=False, default=0)
    mem = models.FloatField(null=False, default=0)
    collect_time = models.DateTimeField(null=False,auto_now_add=True)

    def as_dict(self):
        return {
            'ip': self.ip,
            'cpu': self.cpu,
            'mem': self.mem,
            'collect_time': self.collect_time
        }
