# coding:gbk
from scrapy import cmdline
#导入cmdline模块,可以实现控制终端命令行。
cmdline.execute(['scrapy', 'crawl', 'jobui'])
#用execute（）方法，输入运行scrapy的命令
# scrapy项目的文件夹路径：C:\Users\87408\Desktop\python-c