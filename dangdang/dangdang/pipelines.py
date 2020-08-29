# Define your item pipelines here
# coding: gbk
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl


class DangdangPipeline(object):
    # 定义一个DangdangPipeline类，负责处理item
    def __init__(self):
        # 初始化函数 当类实例化时这个方法会自启动
        self.wb = openpyxl.Workbook()
        # 创建工作薄
        self.ws = self.wb.active
        # 定位活动表
        self.ws.append(['图书名', '作者', '价格', ])
        # 用append函数往表格添加表头

    def process_item(self, item, spider):
        # process_item是默认的处理item的方法，就像parse是默认处理response的方法
        line = [item['name'], item['author'], item['price']]
        # 把图书名、作者、价格都写成列表的形式，赋值给line
        self.ws.append(line)
        # 用append函数把图书名、作者、价格的数据都添加进表格
        return item
        # 将item丢回给引擎，如果后面还有这个item需要经过的itempipeline，引擎会自己调度

    def close_spider(self, spider):
        # close_spider是当爬虫结束运行时，这个方法就会执行
        self.wb.save('C:/Users/87408/Desktop/python-crawler/当当图书.xlsx')
        # 文件夹路径为C:\Users\87408\Desktop\python-crawler，要改为C:/Users/87408/Desktop/python-crawler/
        # 终端输入cd 进入dangdang所在的二级目录，输入scrapy crawl dangdang,文件路径：C:\Users\87408\Desktop\python-crawler\dangdang>
        # 在pipelines、items、setting、bestsellers.py文件中均加入注释# coding: gbk，避免格式出现问题
        # 保存文件
        self.wb.close()
        # 关闭文件
