# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
import MySQLdb
from django.db import connection


class DbUtils(object):


    @staticmethod
    def get_one(sql, param=None):
        cur = connection.cursor()
        cur.execute(sql, param)
        result = cur.fetchone()
        cur.close()
        return result

    @staticmethod
    def get_all(sql, param=None):
        cur = connection.cursor()
        cur.execute(sql, param)
        result = cur.fetchall()
        cur.close()
        return result

    @staticmethod
    def execute_sql(sql, param=None):
        cur = connection.cursor()
        result = cur.execute(sql, param)
        connection.commit()
        cur.close()
        return result
