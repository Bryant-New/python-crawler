import requests
from bs4 import BeautifulSoup

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 总共10页循环10次
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res_books = requests.get(url, headers=headers)
    print(res_books.status_code)
    # 解析数据
    bs = BeautifulSoup(res_books.text, 'html.parser')
    # 缩小搜索范围<ol>标签是<li>标签的父标签，使用find方法只找ol标签
    bs = bs.find('ol', class_="grid_view")
    # 查找豆瓣TOP250对应的序号/电影名/评分/推荐语/链接
    for titles in bs.find_all('li'):
        # 查找序号
        num = titles.find('em', class_="").text
        # 查找电影名
        title = titles.find('span', class_="title").text
        # 查找评分
        comment = titles.find('span', class_="rating_num").text
        # 查找链接
        url_movie = titles.find('a')['href']
        # 查找推荐语
        if titles.find('span',class_="inq") != None:
            tes = titles.find('span', class_="inq").text
            print(num + '.' + title + '__' + tes + '\n' + '推荐语:' + comment + '\n' + url_movie)
        else:
            print(num + '.' + title + '——' + comment + '\n' + '\n' + url_movie)