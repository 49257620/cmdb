from django.db import models, connection
import geoip2.database
import os
from django.conf import settings


# Create your models here.

class AccessLogFile(models.Model):
    name = models.CharField(max_length=128, null=False, default='')
    path = models.CharField(max_length=1024, null=False, default='')
    created_time = models.DateTimeField(null=False, auto_now_add=True)
    status = models.IntegerField(default=0)


class AccessLog(models.Model):
    file_id = models.IntegerField(default=0, null=False)
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    url = models.CharField(max_length=1024, null=False, default='')
    status_code = models.IntegerField(default=0, null=False)
    access_time = models.DateTimeField(null=False)

    @staticmethod
    def get_pie_data(cls, id):
        sql = """
        select status_code ,count(*) from webanalysis_accesslog
        where file_id= %s
        group by status_code
        """
        cur = connection.cursor()
        cur.execute(sql, (id,))
        result = cur.fetchall()
        legend = []
        series = []
        for x in result:
            legend.append(str(x[0]))
            series.append({"name": str(x[0]), "value": str(x[1])})

        return legend, series

    @staticmethod
    def get_bar_data(cls, id):
        sql = """
            select date_format(access_time ,'%%Y-%%m-%%d %%H:00:00') day ,count(*)
            from webanalysis_accesslog
            where file_id= %s
            group by day
            ORDER BY  day
            """
        cur = connection.cursor()
        cur.execute(sql, (id,))
        result = cur.fetchall()
        x = []
        y = []
        for n in result:
            x.append(n[0])
            y.append(n[1])

        return x, y


class AccessLogIps(models.Model):
    ip = models.GenericIPAddressField(null=False, default='0.0.0.0')
    city = models.CharField(max_length=256, null=False, default='')
    latitude = models.FloatField(null=False, default=0)
    longitude = models.FloatField(null=False, default=0)

    @classmethod
    def syncIp(cls):
        sql = """
                    select DISTINCT IP from webanalysis_accesslog a where not exists( select * from webanalysis_accesslogips b where a.ip = b.ip  )
              """
        cur = connection.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        db_path = os.path.join(settings.BASE_DIR,'etc','GeoLite2-City.mmdb')
        for n in result:
            ip = n[0]
            with geoip2.database.Reader(db_path) as reader:
                try:
                    response = reader.city(ip)
                    obj = AccessLogIps()
                    obj.ip = ip
                    obj.city = response.city.names.get('zh-CN', response.city.names.get('en'))
                    obj.latitude = response.location.latitude
                    obj.longitude = response.location.longitude
                    obj.save()
                except BaseException as e:
                    print(ip,e)
                    obj = AccessLogIps()
                    obj.ip = ip
                    obj.city = 'N/A'
                    obj.latitude = 0
                    obj.longitude = 0
                    obj.save()
        cur.close();


