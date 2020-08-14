#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 使用selenium实现可视化操作浏览器的方法：1.获取网页2.输入用户名、密码登录3.点击文章标题，进入评论区发表评论
# 使用selenium提取数据，操作元素

# 导入需要使用的库函数
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import RemoteWebDriver

# 获取用户输入的评论内容
while True:
    comment_content = input('请输入你想要的评论的内容，按回车提交：')
    if comment_content == '':
        print('&'*5, '评论内容不允许为空', '&'*5)
    else:
        break
# 方法一：使用自己电脑上的浏览器
# 实例化浏览器对象
driver = webdriver.Chrome()
# 获取网页
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
# 停顿2秒
time.sleep(2)
# 定位到用户名输入框，输入用户名，使用id：user_login定位到用户输入框
login_name = driver.find_element_by_id('user_login')
# 模拟按键输入用户名spiderman，自动填写表单
login_name.send_keys('spiderman')
# 停顿1秒
time.sleep(1)
# 定位到密码输入框，输入密码，使用id：user_pass定位到密码输入框
password = driver.find_element_by_id('user_pass')
# 模拟按键输入密码crawler334566，自动填写表单
password.send_keys('crawler334566')
# 定位登录按钮，使用id：wp-submit定位到登录框
submit_btn = driver.find_element_by_id('wp-submit')
# 模拟点击登录login元素
submit_btn.click()
# 停顿2秒
time.sleep(2)
# 通过链接的部分文本定位到'《未来已来（三）——同九义何汝秀》'这篇文章
# 获取该文章对应的a标签，并点击文章详情页，寻找id而不是对应的class
# 使用链接文本：未来已来（三）——同九义何汝秀，获取对应文章的超链接
article_link = driver.find_element_by_link_text('未来已来（三）——同九义何汝秀')
# 模拟点击获取文章详情页
article_link.click()

# 进入文章详情页,定位到该页面下编写评论的文本框，输入内容-使用id：comment定位输入评论文本框
comment_area = driver.find_element_by_id('comment')
# 模拟按键输入评论内容，自动填写表单
comment_area.send_keys(comment_content)
# 定位到提交按钮，点击按钮提交评论
comment_submit = driver.find_element_by_id('submit')
# 模拟点击按钮提交评论
comment_submit.click()

# 评论成功10s后关闭浏览器
time.sleep(10)
driver.close()
print('#' * 6, '评论成功，浏览器已关闭', '#' * 6)

