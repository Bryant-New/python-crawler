# Define here the models for your scraped items
# coding£ºutf-8
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopItem(scrapy.Item):
    book_name = scrapy.Field()
    ID_name = scrapy.Field()
    comment = scrapy.Field()
