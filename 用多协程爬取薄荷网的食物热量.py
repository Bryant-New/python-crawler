#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# 选定一个有存储食物热量信息的网站才能爬到数据，薄荷网。它是一个跟健身减肥有关，且可以查询食物数据的网站
# 做项目流程：1.明确目标2.分析过程3.代码实现
# 判断数据储存在哪里，判断数据是否存在html中，是存在html中，不存在HTML中，查看XHR，阅读XHR的name，翻看每个XHR
# 你右击打开“检查”工具，并点击Network，然后刷新页面。点击第0个请求1，看Response。能在Response里找到食物的信息，说明我们想要的数据存在HTML里
# 第0个请求1的Headers，可以发现薄荷网的网页请求方式是get，知道了请求方式是get，我们就知道可以用requests.get()获取数据
# 前10个常见食物分类的网址都是：http://www.boohee.com/food/group/+数字
# 每个食物类别+每一页食物记录网址：http://www.boohee.com/food/view_menu?page=页数，只要改变page后面的数字，就能实现翻页
# 薄荷网的食物热量的数据都存在HTML里，就可以用BeautifulSoup模块来解析
# 右击打开“检查”工具，看Elements，点击光标，把鼠标移到食物【Easy Fun 紫薯营养粥】这里，会发现在<li class="item clearfix">元素下，
# 藏有食物的信息，包括食物详情的链接、食物名和热量,点击href="/shiwu/fdd9b123"，就会跳转到【Easy Fun 紫薯营养粥】的详情页面
# 如果信息不在html网页中，在network中查看XHR，信息存储到XHR中，检查发现请求方式是post的话，就使用request.post获得数据
# 每个食物的信息都被分别藏在了一个<li class="item clearfix">…</li>标签里。每页食物记录里有10个食物，
# 刚好对应上网页源代码里的10个<li class="item clearfix">…</li>标签，
# 用find_all/find就能提取出<li class="item clearfix">…</li>标签下的食物详情链接、名称和热量。
# 提取完数据，我们从csv和openpyxl模块中任意选择使用其中一个模块，把数据存储起来
# 1.获取数据：request.get2.解析数据：BeautifulSoup 3.提取数据；find_all 4.存储数据：csv/oepnpyxl
# 导入需要的库和模块


from gevent import monkey
monkey.patch_all()
# 让程序变成异步模式
import gevent,requests, bs4, csv
from gevent.queue import Queue
# 导入所需模块，并根据前面分析得出的网址规律，
# 用for循环构造出前3个常见食物类别的前3页食物记录的网址和
# 第11个常见食物类别的前3页食物记录的网址，并把这些网址放进队列，打印出来

# 创建队列对象,并赋值给work
work = Queue()
# 前三个常见食物分类的前三页的食物记录网址：
url_1 = 'https://www.boohee.com/food/group/{type}?page={page}'
# 通过两个for循环，设置分类的数字和页数的数字
# 把构造好的网址用put_nowait方法添加进队列中
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)

print(work)



