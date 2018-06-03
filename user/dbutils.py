#encoding: utf-8
import traceback

import MySQLdb


class DbUtils(object):

    MYSQL_HOST = '47.104.188.243'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1qaz@WSX'
    MYSQL_DB = 'cmdb_lw'
    MYSQL_CHARSET = 'utf8'

    @staticmethod
    def execute_sql(sql, args=(), fetch=True, one=False):
        cnt, result = 0, None
        conn, cur = None, None
        try:
            conn = MySQLdb.connect(host=DbUtils.MYSQL_HOST, port=DbUtils.MYSQL_PORT, user=DbUtils.MYSQL_USER, passwd=DbUtils.MYSQL_PASSWORD, db=DbUtils.MYSQL_DB, charset=DbUtils.MYSQL_CHARSET)
            cur = conn.cursor()
            cnt = cur.execute(sql, args)
            if fetch:
                result = cur.fetchone() if one else cur.fetchall()
            else:
                conn.commit()
        except BaseException as e:
            print(e)
            print(traceback.format_exc())
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

        return cnt, result
