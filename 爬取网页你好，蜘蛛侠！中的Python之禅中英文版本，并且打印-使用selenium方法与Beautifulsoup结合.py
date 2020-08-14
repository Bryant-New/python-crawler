#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 练习使用selenium爬取动态网页的信息，练习selenium与BeautifulSoup的搭配使用
# selenium库使用说明：https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

# 导入需要使用的库函数
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# 你好，蜘蛛侠！是一个动态网页，URL：https://localprod.pandateacher.com/python-manuscript/hello-spiderman/
# Python之禅的内容没有存在网页源代码中，无法通过requests.get()与BeautifulSoup提取“Python之禅”的内容，不过，我们可以通过selenium获取到
# 1.使用selenium获取网页2.输入喜欢的老师和助教3.获取elements中渲染完成完整网页源代码的中英文对照
# 先用`selenium`获取到渲染完成的`Elements`中的网页源代码，然后，`BeautifulSoup`登场解析和提取数据。
# 声明浏览器对象
driver = webdriver.Chrome()
# 使用实例化的浏览器对象获取目标网页
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# 暂停两秒，等待浏览器缓冲
time.sleep(2)
teacher = driver.find_element_by_id('teacher')  # 定位到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀') # 输入文字
assistant = driver.find_element_by_name('assistant')  # 定位到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢') # 输入文字
button = driver.find_element_by_class_name('sub')  # 定位到【提交】按钮
button.click()  # 点击【提交】按钮
time.sleep(1)  # 等待一秒
# 使用selenium的page_source方法可以直接返回页面源码
pageSourece = driver.page_source
# 使用bs解析网页
soup = BeautifulSoup(pageSourece, 'html.parser')
# 找到源代码Python之禅中文版和英文版所在的元素class=content
contents = soup.find_all(class_="content")
for content in contents:  # 遍历列表
    title = content.find('h1').text  #  提取标题
    chan = content.find('p').text.replace(' ', '')  # 提取Python之禅的正文，并且去掉文字前面的所有空格
    print(title + chan + '\n')  # 打印Python之禅的标题与正文
driver.close()