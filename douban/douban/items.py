# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # ����һ����DoubanItem�����̳���scrapy.Item
    title = scrapy.Field()
    # ������������������
    publish = scrapy.Field()
    # ���������Ϣ����������
    score = scrapy.Field()
    # �������ֵ���������