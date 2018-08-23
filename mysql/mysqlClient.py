# -*- coding: utf-8 -*-

import pymysql


class MysqlClient:
    def __init__(self, host=None, db=None):        
        self.host = host
        # 使用时修改用户名与密码
        self.user = ''
        self.passwd = ''        
        self.db = db
        self.charset = 'utf8'
        self.__conn = self._connect()

    def _connect(self):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        return conn   

    def exec_sql(self, sql):
        cursor = self.__conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        self.__conn.close()

