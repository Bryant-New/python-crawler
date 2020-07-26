# 引用requests模块
import requests
# 引用bs4模块
from bs4 import BeautifulSoup
# 引用urllib模块
from urllib.request import quote
# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

movie = input('你想看什么电影啊？')
# 将汉字用gbk格式编码，赋值给gbkmovie
gbkmovie = movie.encode('gbk')
# 将gbk格式的内容转化为url，然后前半部分主网站网址拼接起来
url = 'http://s.ygdy8.com/plus/s0.php?typeid=1&keyword=' + quote(gbkmovie)
print(url)
# 下载xx电影的搜索页面
res = requests.get(url, headers=headers)
# 定义res的编码类型
res.encoding = 'gbk'
# 解析网页
soup_movie = BeautifulSoup(res.text, 'html.parser')
# 寻找下载网页
urlpart = soup_movie.find(class_='co_content8').find_all('table')
print(urlpart)
if urlpart:
    urlpart = urlpart[0].find('a')['href']
    urlmovie = 'https://www.ygdy8.com/' + urlpart
    res1 = requests.get(urlmovie)
    res1.encoding('gbk')
    soup_movie1 = BeautifulSoup(res1.text, 'html.parser')
    urldownload =soup_movie1.find('div', id="Zoom").find('span').find('table').find('a')['href']
    print(urldownload)
else:
    # 针对某些没有电影的链接
    print('没有'+movie)
