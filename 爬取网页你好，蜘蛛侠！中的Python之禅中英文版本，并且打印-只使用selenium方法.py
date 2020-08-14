#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 练习使用selenium爬取动态网页的信息，练习selenium与BeautifulSoup的搭配使用
# selenium库使用说明：https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

# 导入需要使用的库函数
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 调用Option模块
from selenium.webdriver.chrome.webdriver import RemoteWebDriver  # 从selenium库中调用RemoteWebDriver模块

# 你好，蜘蛛侠！是一个动态网页，URL：https://localprod.pandateacher.com/python-manuscript/hello-spiderman/
# Python之禅的内容没有存在网页源代码中，无法通过requests.get()与BeautifulSoup提取“Python之禅”的内容，不过，我们可以通过selenium获取到
# 1.使用selenium获取网页2.输入喜欢的老师和助教3.获取elements中渲染完成完整网页源代码的中英文对照
# 声明浏览器对象
driver = webdriver.Chrome()
# 使用实例化的浏览器对象获取目标网页
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# 暂停2min
time.sleep(2)

# 定位到【请输入你喜欢的老师】下面的输入框位置对应html源代码，id：teacher
teacher = driver.find_element_by_id('teacher')
# 模拟输入:喜欢的老师名字：吴枫
teacher.send_keys('吴枫')
# 定位到【请输入你喜欢的助教】下面的输入框位置对应html源代码，id：assistant
assistant = driver.find_element_by_id('assistant')
# 模拟输入:喜欢的助教名字：酱酱
assistant.send_keys('酱酱')
# 定位到提交-按钮位置对应html源代码，class：sub通过class name定位元素
button = driver.find_element_by_class_name('sub')
# 点击【提交】按钮
button.click()
time.sleep(1)

# 定位到Python之禅位置对应html源代码，class：content通过class name定位元素
contents = driver.find_elements_by_class_name('content')
# 提取标题
for content in contents:
    # 使用h1标签名提取标题-方法：find_element_by_tag_name.text
    title = content.find_element_by_tag_name('h1').text
    # ,使用p标签名提取正文-方法：find_element_by_tag_name.text
    chan = content.find_element_by_tag_name('p').text
    print(title+'\n'+chan+'\n')
driver.close()