from ProxyPool.db import MySqlClient
from ProxyPool.testproxy import checkproxy
from ProxyPool.crawler import Crawler

mysql=MySqlClient()
def checkmysql():
    print('数据库检查开始')
    proxies=mysql.all()
    if proxies:
        for proxy in proxies:
            if not checkproxy(proxy[0],proxy[1]):
                mysql.delete(proxy[0])
    print('数据库检查完成')



def addproxy():
    print('开始添加代理')
    lists=[]
    Crawler().getAllproxy(lists)
    for list in lists:
        mysql.add(list[0],list[1])
    print('代理添加完成')

def main():
    checkmysql()
    addproxy()

main()