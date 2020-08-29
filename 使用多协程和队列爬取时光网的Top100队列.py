# coding: gbk
# python在安装时，默认的编码是ascii，当程序中出现非ascii编码时，
# python的处理常常会报这样的错UnicodeDecodeError: 'ascii' codec can't decode byte 0x??
# in position 1: ordinal not in range(128)，python没办法处理非ascii编码的，此时需要自己设置将python的默认编码，一般设置为utf8的编码格式
# str转bytes叫encode，bytes转str叫decode,print()函数自身有限制，不能完全打印所有的unicode字符。
# 使用多协程和队列，爬取时光网电视剧TOP100的数据（剧名、导演、主演和简介），并用csv模块将数据存储下来。
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
from gevent import monkey
monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue


work = Queue()
url_1 = 'http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_1)

url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for x in range(1,11):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)

def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers, )
        bs_res = bs4.BeautifulSoup(res.text,'html.parser')
        datas = bs_res.find_all('div',class_="mov_con")
        for data in datas:
            TV_title = data.find('a').text
            data = data.find_all('p')
            TV_data =''
            for i in data:
                TV_data =TV_data + ''+ i.text
            writer.writerow([TV_title,TV_data])
            print([TV_title, TV_data])

csv_file = open('电视剧1.txt', 'w', newline='', encoding='utf-8')
# 存为.csv中文会出现乱码，英文不会乱码，存成.txt文件不会乱码
writer = csv.writer(csv_file)

task_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)