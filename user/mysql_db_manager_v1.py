# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
import MySQLdb


class DbUtils(object):

    MYSQL_HOST = '47.104.188.243'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1qaz@WSX'
    MYSQL_DB = 'cmdb_lw'
    MYSQL_CHARSET = 'utf8'

    @staticmethod
    def get_conn():
        return MySQLdb.connect(host=DbUtils.MYSQL_HOST, port=DbUtils.MYSQL_PORT, user=DbUtils.MYSQL_USER, passwd=DbUtils.MYSQL_PASSWORD, db=DbUtils.MYSQL_DB,
                               charset=DbUtils.MYSQL_CHARSET)

    @staticmethod
    def get_one(sql, param=None):
        conn = DbUtils.get_conn()
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(sql, param)
        result = cur.fetchone()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def get_all(sql, param=None):
        conn = DbUtils.get_conn()
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(sql, param)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def execute_sql(sql, param=None):
        conn = DbUtils.get_conn()
        cur = conn.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute(sql, param)
        conn.commit()
        cur.close()
        conn.close()
        return result
