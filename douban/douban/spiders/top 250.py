# coding:gbk
import scrapy
import bs4
from ..items import DoubanItem
# ��Ҫ����DoubanItem������items���档��Ϊ��items��top250.py����һ��Ŀ¼������Ҫ��..items������һ���̶��÷���

class DoubanSpider(scrapy.Spider):
#����һ��������DoubanSpider��
    name = 'douban'
    #�������������Ϊdouban��
    allowed_domains = ['book.douban.com']
    #����������ȡ��ַ��������
    start_urls = []
    #������ʼ��ַ��
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)
        #�Ѷ���Top250ͼ���ǰ3ҳ��ַ��ӽ�start_urls��

    def parse(self, response):
    #parse��Ĭ�ϴ���response�ķ�����
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        #��BeautifulSoup����response��
        datas = bs.find_all('tr',class_="item")
        #��find_all��ȡ<tr class="item">Ԫ�أ����Ԫ���ﺬ���鼮��Ϣ��
        for data in  datas:
        #����data��
            item = DoubanItem()
            #ʵ����DoubanItem����ࡣ
            item['title'] = data.find_all('a')[1]['title']
            #��ȡ������������������ݷŻ�DoubanItem���title�����
            item['publish'] = data.find('p',class_='pl').text
            #��ȡ��������Ϣ������������ݷŻ�DoubanItem���publish�
            item['score'] = data.find('span',class_='rating_nums').text
            #��ȡ�����֣�����������ݷŻ�DoubanItem���score�����
            print(item['title'])
            #��ӡ������
            yield item
            #yield item�ǰѻ�õ�item���ݸ����档