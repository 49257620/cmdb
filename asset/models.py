from django.db import models


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

    created_time = models.DateTimeField(null=False)
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
