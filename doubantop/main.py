# coding:utf-8
# 为了避免编码出现问题，所有的.py文件包括：settings.py、pipelines.py、items.py、comments.py、main.py
# 都加上# coding:utf-8，避免出现英文乱码
from scrapy import cmdline
cmdline.execute(['scrapy', 'crawl', 'doubantop'])