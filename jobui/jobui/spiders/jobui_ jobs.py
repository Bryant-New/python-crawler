# coding: gbk
import scrapy
import bs4
from ..items import JobuiItem


class JobuiSpider(scrapy.Spider):
    # ����һ��JobuiSpider������
    name = 'jobui'
    # �������������Ϊjobui
    allowed_domain = ['www.jobui.com']
    # ��������������ȡ��ַ����������ְ�Ѽ���վ������
    start_urls = ['https://www.jobui.com/rank/company/']
    # ������ʼ��ַ����ְ�Ѽ���ҵ���а����ַ


    def parse(self, response):
        # parse��Ĭ�ϴ���response�ķ���
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # ��BeautifulSoup����response����ҵ���а����ҳԴ���룩
        ul_list = bs.find_all('ul', class_='textList flsty cfix')
        # ��find_all��ȡ<ul class_="textList flsty cfix">��ǩ
        for ul in ul_list:
            a_list = ul.find_all('a')
            # ��find_all��ȡ��<ul class_="textList flsty cfix">Ԫ���������<a>Ԫ��
            for a in a_list:
                company_id = a['href']
                # ��ȡ������<a>Ԫ�ص�href���Ե�ֵ��Ҳ���ǹ�˾id��ʶ
                url = 'https://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
                # �������˾��Ƹ��Ϣ����ַ����
                yield scrapy.Request(real_url, callback=self.parse_job)
                # ��yield���ѹ���õ�request���󴫵ݸ����档��scrapy.Request����request����callback�������õ���parsejob����



    def parse_job(self, response):
        # �����µĴ���response�ķ���parse_job�����������ֿ����Լ���
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        # ��BeautifulSoup����response(��˾��Ƹ��Ϣ����ҳԴ����)
        company = bs.find(id="companyH1").text
        # ��find������ȡ����˾����
        datas = bs.find_all('div', class_="c-job-list")
        # ��find_all��ȡ<div class_="c-job-list">��ǩ�����溬����Ƹ��Ϣ������
        for data in datas:
            item = JobuiItem()
            # ʵ����JobuiItem�����
            item['company'] = company
            # �ѹ�˾���ƷŻ�JobuiItem���company������
            item['position'] = data.find('a').find('h3').text
            # ��ȡ��ְλ���ƣ�����������ݷŻ�JobuiItem���position������
            item['address'] = data.find_all('span')[0]['title']
            # ��ȡ�������ص㣬����������ݷŻ�JobuiItem���address������
            item['detail'] = data.find_all('span')[1]['title']
            # ��ȡ����ƸҪ�󣬲���������ݷŻ�JobuiItem���detail������
            yield item
            # ��yield����item���ݸ�����