
import re
import requests
from ProxyPool.testproxy import checkproxy
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

class Crawler(object):
    def get_page(self,url):
        """
        抓取代理
        :param url:
        :param options:
        :return:
        """
        headers =base_headers
        print('正在抓取', url)
        try:
            response = requests.get(url, headers=headers)
            print('抓取成功', url, response.status_code)
            if response.status_code == 200:
                return response.text
        except ConnectionError:
            print('抓取失败', url)
            return None
    #爬取66ip的代理
    def crawl_daili66(self, lists,page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('正在爬取66ip')
            html = self.get_page(url)
            if html:
                ips=re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>',html)
                ports=re.findall(r'<td>(\d+)</td>',html)
                for ip, port in zip(ips, ports):
                    if checkproxy(ip,port):
                        lists.append([ip,port])
    #爬取ip3366的代理
    def crawl_ip3366(self,lists):
        for i in range(1, 4):
            start_url = 'http://www.ip3366.net/?stype=1&page={}'.format(i)
            html = self.get_page(start_url)
            if html:
                print('正在爬取ip3366')
                #table = re.find(r'<div id="list">.*?</div>', html)
                ips = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>', html)
                ports = re.findall(r'<td>(\d+)</td>', html)
                for ip, port in zip(ips, ports):
                    if checkproxy(ip, port):
                        lists.append([ip, port])
    #爬取kuaidaili的代理
    def crawl_kuaidaili(self,lists):
        for i in range(1, 4):
            start_url = 'http://www.kuaidaili.com/free/inha/{}/'.format(i)
            html = self.get_page(start_url)
            if html:
                print('正在爬取kuaidaili')
                ips = re.findall(r'<td data-title="IP">(\d+\.\d+\.\d+\.\d+)</td>', html)
                ports = re.findall(r'<td data-title="PORT">(\d+)</td>', html)
                for ip, port in zip(ips, ports):
                    if checkproxy(ip, port):
                        lists.append([ip, port])

    def getAllproxy(self,lists):
        self.crawl_daili66(lists)
        self.crawl_ip3366(lists)
        self.crawl_kuaidaili(lists)