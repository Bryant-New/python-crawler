# Define your item pipelines here
# coding: gbk
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl


class JobuiPipeline(object):
    # ����һ��JobuiPipeline�࣬������item
    def __init__(self):
        # ��ʼ������ ����ʵ����ʱ���������������
        self.wb = openpyxl.Workbook()
        # ����������
        self.ws = self.wb.active
        # ��λ���
        self.ws.append(['��˾', 'ְλ', '��ַ', '��Ƹ��Ϣ'])
        # ��append�����������ӱ�ͷ

    def process_item(self, item, spider):
        # process_item��Ĭ�ϵĴ���item�ķ���������parse��Ĭ�ϴ���response�ķ���
        line = [item['company'], item['position'], item['address'], item['detail']]
        # �ѹ�˾���ơ�ְλ���ơ������ص����ƸҪ��д���б����ʽ����ֵ��line
        self.ws.append(line)
        # ��append�����ѹ�˾���ơ�ְλ���ơ������ص����ƸҪ������ݶ���ӽ����
        return item
        # ��item���ظ����棬������滹�����item��Ҫ������itempipeline��������Լ�����

    def close_spider(self, spider):
        # close_spider�ǵ������������ʱ����������ͻ�ִ��
        self.wb.save('C:/Users/87408/Desktop/python-crawler/������ҵ��Ƹ��Ϣ.xlsx')
        # �ļ���·��ΪC:\Users\87408\Desktop\python-crawler��Ҫ��ΪC:/Users/87408/Desktop/python-crawler/
        # �ն�����cd ����jobui���ڵĶ���Ŀ¼������scrapy crawl jobui,�ļ�·����C:\Users\87408\Desktop\python-crawler\jobui>
        # ��pipelines��items��setting��jobui_jobui.py�ļ��о�����ע��# coding: gbk�������ʽ��������
        # �����ļ�
        self.wb.close()
        # �ر��ļ�
