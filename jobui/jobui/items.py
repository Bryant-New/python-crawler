# Define here the models for your scraped items
# coding: gbk
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobuiItem(scrapy.Item):
    # ������һ���̳���scrapy.Item��JobuiItem��
    company = scrapy.Field()
    # ���幫˾���Ƶ���������
    position = scrapy.Field()
    # ����ְλ���Ƶ���������
    address = scrapy.Field()
    # ���幤���ص����������
    detail = scrapy.Field()
    # ������ƸҪ�����������