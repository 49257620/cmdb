from django.db import models,connection


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
    def get_pie_data(cls,id):
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
            series.append({"name":str(x[0]),"value":str(x[1])})

        return legend,series

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
