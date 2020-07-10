import pymysql
from ProxyPool.setting import *
from random import choice
import re


class MySqlClient(object):
    # 初始化
    def __init__(self, host=HOST, port=MYSQL_PORT, username=MYSQL_USERNAME, password=MYSQL_PASSWORD, sqlname=SQL_NAME):
        self.db = pymysql.connect(host=host, user=username, password=password, port=port, db=sqlname)
        self.cursor = self.db.cursor()

    # 添加代理IP
    def add(self, ip,port):
        sql_add = "INSERT INTO PROXY (IP,PORT) VALUES ('%s', '%s')" % (ip, port)
        if not self.exists(ip):
            self.cursor.execute(sql_add)
            self.db.commit()

    # 删除代理IP
    def delete(self, ip):
        sql_delete = "delete from PROXY where IP='%s'" % (ip)
        self.cursor.execute(sql_delete)
        self.db.commit()
    # 随机获取有效代理
    def random(self):
        # 先从满分中随机选一个
        sql = "SELECT * FROM PROXY "
        if self.cursor.execute(sql):
            results = self.cursor.fetchall()
            #随机化results
            return choice(results)
    # 判断是否存在
    def exists(self, ip):
        sql_exists = "SELECT 1 FROM PROXY WHERE IP='%s' limit 1" % ip
        return self.cursor.execute(sql_exists)
        
    # 获取数量
    def count(self):
        sql_count = "SELECT * FROM PROXY"
        return self.cursor.execute(sql_count)

    # 获取全部
    def all(self):
        self.count()
        return self.cursor.fetchall()

    # 批量获取
    def batch(self, start, stop):
        sql_batch = "SELECT * FROM PROXY LIMIT %s, %s" % (start, stop - start)
        self.cursor.execute(sql_batch)
        return self.cursor.fetchall()
