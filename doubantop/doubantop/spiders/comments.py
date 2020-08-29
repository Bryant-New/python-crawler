# comments.py文件里编写spider
# coding:utf-8
# 创建scrapy文件；终端-terminal输入命令：scrapy startproject doubantop
# 在使用命令行startproject的时候，会自动生成scrapy.cfg。而使用命令行cmd启动爬虫时，
# crawl会去搜索cmd当前目录下的scrapy.cfg文件，官方文档中也进行了说明。找不到scrapy.cfg文件则认为没有该project
# split（）方法在使用指定的分隔符将给定字符串断开后，返回字符串列表。
# data.find_all('a')[1]['href']获取a标签中的href值
# text.split()网页中的文字用空格分开，提取第0个的标签
import scrapy,bs4
from ..items import DoubantopItem

class DoubantopSpider(scrapy.Spider):
    name = 'doubantop'
    allowed_domins = ['https://book.douban.com']
    start_urls = []
    for x in range(2):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        datas = soup.find_all('tr',class_='item')
        for data in datas:
            book_url = data.find_all('a')[1]['href']
            comment_url = book_url+'comments/'
            yield scrapy.Request(comment_url,callback=self.parse_comment)


    def parse_comment(self,response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        book_name = soup.find('div',id='content').text.split()[0]
        datas = soup.find_all('div',class_='comment')
        for data in datas:
            item = DoubantopItem()
            item['book_name'] = book_name
            item['ID_name'] = data.find_all('a')[1].text
            item['comment'] = data.find('span',class_='short').text
            yield item