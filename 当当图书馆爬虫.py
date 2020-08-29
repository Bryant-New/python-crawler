# coding: gbk
# 爬取当当网2018年图书销售榜单前3页的数据（图书名、作者和书的价格）。
# 当当网2018年图书销售榜单链接：http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-1
# 使用Scrapy，爬取当当网2018年图书销售榜单前3页的数据（图书名、作者和书的价格）。
# 创建scrapy项目-要保存项目的目录下，输入创建Scrapy项目的命令：scrapy startproject dangdang
# 可以在items.py文件里定义item；在bestsellers.py文件里编写spider；在settings.py文件里修改设置；在main.py文件里写入运行scrapy的代码，点击运行
# li标签没有属性不好定位，不用它做父标签，选择一个最近的有class属性作为父标签
# 选择'ul', class_="bang_list clearfix bang_list_mode"中再选li标签
