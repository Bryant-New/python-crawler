#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
import requests
import json


# 使用cookies保存登录状态，不需要重复输入账号、密码
# 用requests.session()创建session对象，相当于创建了一个特定的会话，帮我们自动保持了cookies。
session = requests.session()
# 反爬虫机制，封装header
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# 使用Python模拟浏览器向网站服务器发起登录请求
# 把有关登录的参数封装成字典赋值给data
try:
# 如果能读到cookies文件，执行以下代码，跳过except代码，不用登录就能发表评论
    # 以reader读取模式，打开名为cookies.txt文件
    cookies_txt = open('cookies.txt', 'r')
    # 调用json模块的loads函数，把字符串转成字典
    cookies_dict = json.loads(cookies_txt.read())
    # 把转成字典的cookies再转成cookies本来的格式
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    # 获取cookies:调用requests对象（session）的cookies属性
    session.cookies = cookies
except FileExistsError:
# 如果读取不到cookies文件，程序报“FileNotFoundError(找不到文件)的错，执行以下代码，重新登录获取
    # 登录网址
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    # 登录参数
    data = {
        'log': input('请输入账号'),  # 写入账户
        'pwd': input('请输入密码'),  # 写入密码
        'wp-submit': '登录',  # 登录按钮
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',  # 成功登录后跳转的网址，即原网站网址-爬虫练习网站
        'testcookie': '1'
    }
    # 在创建的session下用post发起登录请求，放入参数：请求登录的网址、请求头和登录参数
    session.post(url, headers=headers, data=data)
    # 把cookies转化成字典
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookies_dict)
    # 调用json模块中地dumps函数，把cookies从字典转成字符串
    cookies_str = json.dumps(cookies_dict)
    print(cookies_str)
    # 创建名为cookies.txt文件，以写入模式写入内容
    f = open('cookies.txt', 'w')
    # 把已经转成字符串的cookies写入文件。
    f.write(cookies_str)
    # 关闭文件
    f.close()
# 向网页提交表单数据
# 返回200的状态码，意味着服务器接受到并响应了登录请求，进行了成功登录
# 提取，调用登录的cookie
# 提取cookies的方法：调用requests对象（login_in）的cookies属性获得登录的cookies，并赋值给变量cookies。
# 想要评论的文章网址
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# 获取评论参数-把有关评论的参数封装成字典
data_1 ={
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',  # 发表评论的按钮
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# 用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
# 调用cookies的方法就是在post请求中传入cookies=cookies的参数。
comment = session.post(url_1, headers=headers, data=data_1)
print(comment.status_code)
# 发表博客评论的三个重点：1.post带参数地请求登录2.获得登录地cookies3.带cookies去请求发表评论
# 创建session来进一步优化cookies
# 程序读取到cookies，就自动登录，发表评论，如果读取不到，就重新输入账号密码登录，再评论
