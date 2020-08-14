#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 当你遇到验证码很复杂的网站时，selenium允许让人去手动输入验证码，然后把剩下的操作交给机器。
# selenium-强大的Python库。用几行代码，控制浏览器，做出自动打开、输入、点击等操作，就像是有一个真正的用户在操作一样。
# 那些交互复杂、加密复杂的网站，selenium问题简化，爬动态网页如爬静态网页一样简单。
# 静态网页-html写出得网页，使用使用BeautifulSoup爬取这类型网页，网页源代码中就包含着网页的所有信息，网页地址栏的URL就是网页源代码的URL
# 静态网页-HTML源代码与渲染完成得Elements源代码一样，动态网页：如QQ音乐，爬取的数据不在HTML源代码中，而是在json中，能直接使用网址栏的URL
# 动态网页-需要找到json数据的真实URL。有的数据没有存在HTML源码中，URL加密逻辑复杂的情况时，selenium就派上了用场，它可以真实地打开一个浏览器，
# 动态网页-当网页不断发生跳转时而对应网页地址栏中的网页没有变化，则为动态网页
# 等待所有数据都加载到Elements中之后，再把这个网页当做静态网页爬取就好了。速度较慢
# 本地谷歌浏览器设置方法
# #从selenium库中调用webdriver模块
from selenium import webdriver
import time

# selenium如何获取、解析与提取数据
# 设置引擎为Chrome，真实地打开一个Chrome浏览器，把Chrome浏览器设置为引擎，然后赋值给变量driver，driver是实例化的浏览器
driver = webdriver.Chrome()
# 使用selenium获取数据，get(URL)是webdriver的一个方法，它的使命是为你打开指定URL的网页。
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# 等待2秒，是由于浏览器缓冲加载网页需要耗费一些时间，
time.sleep(2)

# 解析数据-selenium所解析提取的，是Elements中的所有数据，而BeautifulSoup所解析的则只是Network中第0个请求的响应。
# 使用BeautifulSoup解析提取数据时，首先要把Response对象解析为BeautifulSoup对象，然后再从中提取数据。
# 用selenium把网页打开，所有信息就都加载到了Elements那里，之后，就可以把动态网页用静态网页的方法爬取了。
# 在selenium中，获取到的网页存在了driver中，而后，解析与提取是同时做的，都是由driver这个实例化的浏览器完成。
# 找到【请输入你喜欢的老师】下面的输入框位置
teacher = driver.find_element_by_id('teacher')

# 提取出的数据属于WebElement类对象，如果直接打印它，返回的是一串对它的描述，
# WebElement类对象与Tag对象类似，它也有一个方法，可以通过属性名提取属性的值，这个方法是.get_attribute()。
# 获取url-转成字符串-变成 WebElement对象-再转成字符串
# 提取多个元素的方法-find_element_by_与BeautifulSoup中的find类似，可以提取出网页中第一个符合要求的元素
# .send_keys() # 模拟按键输入，自动填写表单
teacher.send_keys('必须是吴枫呀')  # 输入文字
assistant = driver.find_element_by_name('assistant')  # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢')  # 输入文字
time.sleep(2)
button = driver.find_element_by_class_name('sub')  # 找到【提交】按钮
time.sleep(1)
# 点击元素
button.click()  # 点击【提交】按钮
time.sleep(1)
# driver.close()是关闭浏览器驱动，每次调用了webdriver之后，都要在用完它之后加上一行driver.close()用来关闭它
# 使用selenium调用了浏览器之后也要记得关闭浏览器
driver.close()

