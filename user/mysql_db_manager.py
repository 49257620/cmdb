# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’
import MySQLdb

MYSQL_HOST = '47.104.188.243'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1qaz@WSX'
MYSQL_DB = 'cmdb_lw'
MYSQL_CHARSET = 'utf8'


def get_conn():
    return MySQLdb.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB,
                           charset=MYSQL_CHARSET)


def get_one(sql, param=None):
    conn = get_conn()
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, param)
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result


def get_all(sql, param=None):
    conn = get_conn()
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql, param)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result


def execute_sql(sql, param=None):
    conn = get_conn()
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    result = cur.execute(sql, param)
    conn.commit()
    cur.close()
    conn.close()
    return result
