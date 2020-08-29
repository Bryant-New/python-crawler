# Define your item pipelines here
# coding: gbk
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl


class DangdangPipeline(object):
    # ����һ��DangdangPipeline�࣬������item
    def __init__(self):
        # ��ʼ������ ����ʵ����ʱ���������������
        self.wb = openpyxl.Workbook()
        # ����������
        self.ws = self.wb.active
        # ��λ���
        self.ws.append(['ͼ����', '����', '�۸�', ])
        # ��append�����������ӱ�ͷ

    def process_item(self, item, spider):
        # process_item��Ĭ�ϵĴ���item�ķ���������parse��Ĭ�ϴ���response�ķ���
        line = [item['name'], item['author'], item['price']]
        # ��ͼ���������ߡ��۸�д���б����ʽ����ֵ��line
        self.ws.append(line)
        # ��append������ͼ���������ߡ��۸�����ݶ���ӽ����
        return item
        # ��item���ظ����棬������滹�����item��Ҫ������itempipeline��������Լ�����

    def close_spider(self, spider):
        # close_spider�ǵ������������ʱ����������ͻ�ִ��
        self.wb.save('C:/Users/87408/Desktop/python-crawler/����ͼ��.xlsx')
        # �ļ���·��ΪC:\Users\87408\Desktop\python-crawler��Ҫ��ΪC:/Users/87408/Desktop/python-crawler/
        # �ն�����cd ����dangdang���ڵĶ���Ŀ¼������scrapy crawl dangdang,�ļ�·����C:\Users\87408\Desktop\python-crawler\dangdang>
        # ��pipelines��items��setting��bestsellers.py�ļ��о�����ע��# coding: gbk�������ʽ��������
        # �����ļ�
        self.wb.close()
        # �ر��ļ�
