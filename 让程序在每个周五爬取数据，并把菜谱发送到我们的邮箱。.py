#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# 可以根据我们设定的时间自动爬取数据；第二是通知功能，即程序可以把爬取到的数据结果以邮件的形式自动发送到我们的邮箱。
# 自动爬取每日的天气，并定时把天气数据和穿衣提示发送到你的邮箱

# 程序三个功能块：1.爬虫2.邮件3.定时
# 爬虫-邮件通知，使用smtplib和email库，定时功能-schedule库
# 百度天气网址：http://www.weather.com.cn/weather/101280601.shtml，点击"右键"——"检查"——"Network"，刷新页面，点看第0个请求
# 数据放在HTML里，没问题。那我们点击Elements，温度数据放在<p class="tem">之下。“小雨”所在的位置是<p title="小雨" class="wea">小雨</p>
# 网页源代码里面搜索观察了一番，发现可以使用class="wea"和class="tem"来匹配目标数据，网页源码出现乱码-用response.encoding属性，
# 在网页上点击"右键"——"查看网页源代码"，会弹出一个新的标签页，然后搜索charset，查看一下编码方式,网页是用utf-8编码的。
# 用response.encoding转换一下编码

# 爬虫-邮件-定时
import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input("请输入你的邮箱:")
password = input("请输入你的密码:")
receiver = input('请输入收件人的邮箱：')


def recipe_spider():
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.125 Safari/537.36'
    }
    res_foods = requests.get('http://www.xiachufang.com/explore/')
    bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
    list_foods = bs_foods.find_all('div', class_='info pure-u')
    list_all = ''
    num = 0
    for food in list_foods:
        num = num+1
        tag_a = food.find('a')
        name = tag_a.text.strip()
        url = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p', class_='ing ellipsis')
        ingredients = tag_p.text.strip()
        food_info = '''
    
        序号: %s
        菜名: %s
        链接: %s
        原料: %s
         '''%(num, name, url, ingredients)
        list_all = list_all+food_info
    return list_all


def send_email(list_all):
    global account, password, receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(account, password)
    content = '亲爱的，本周的热门菜谱如下：'+list_all
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '周末吃个啥'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('发送邮件失败')


def job():
    print('开始一次任务')
    list_all = recipe_spider()
    send_email(list_all)
    print('任务完成')


schedule.every().friday.at("18:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
