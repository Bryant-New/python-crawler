#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# 可以根据我们设定的时间自动爬取数据；第二是通知功能，即程序可以把爬取到的数据结果以邮件的形式自动发送到我们的邮箱。
# 自动爬取每日的天气，并定时把天气数据和穿衣提示发送到你的邮箱

from gevent import monkey
# 从gevent库种导入monkey模块
monkey.patch_all()
# monkey.patch_all()能把程序变成协作式运行，帮助程序实现异步
import gevent, time, requests
# 导入gevent、time、requests
from gevent.queue import Queue
# 从gevent库中导入quue模块


start = time.time()

url_list = [
'https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/'
]

work = Queue()
# 用Queue()能创建queue对象，相当于创建了一个不限任何存储数量的空队列
for url in url_list:
# 遍历url_list
    work.put_nowait(url)
    # 用put_nowait()函数，创建了queue对象后，我们就能调用这个对象的put_nowait方法，把我们的每个网址都存储进我们刚刚建立好的空队列里


def crawler():
    while not work.empty():
    # 当队列不是空的时候，就执行下面的程序
        url = work.get_nowait()
        # 用get_nowait()函数可以把队列里的网址取出来
        r = requests.get(url)
        # 用requests.get()函数抓取网址。
        print(url, work.qsize(), r.status_code)
        # 打印网址、队列长度、抓取请求的状态码。


tasks_list = [ ]
# 创建空的任务列表
for x in range(2):
# 相当于创建了2个爬虫
    task = gevent.spawn(crawler)
    # 用gevent.spawn()函数执行crawler()函数的任务
    tasks_list.append(task)
    # 往任务列表里添加任务
gevent.joinall(tasks_list)
# 用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站
end = time.time()
print(end-start)