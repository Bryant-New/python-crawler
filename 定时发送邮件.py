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
# 导入需要使用的库函数
import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time

# 定义account、password和receiver为全局变量，即用input()获取到的数据
# 获取邮箱账号
account = input('请输入你的邮箱：')
# 获取邮箱密码
password = input('请输入你的密码：')
# 获取收件人的邮箱
receiver = input('请输入收件人的邮箱：')


# 多行代码，将其封装成函数，进行使用
def weather_spider():
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    # 选择好你所在地区的天气网址来替换这段代码中的URL。General中的url,html源码中对应的第0个请求
    url = 'http://www.weather.com.cn/weather/101310101.shtml'
    res = requests.get(url, headers=headers)
    # 原网页是用utf-8方式编码的，res默认是用AscII码编码，若要避免乱码，所以要用encoding语句将编码方式进行转换
    res.encoding = 'utf-8'
    print(res.status_code)
    # 打印请求返回的html网页源代码-res.text
    # print(res.text)
    # 使用Beautifulsoup提取和解析数据
    # 把网页解析为BeautifulSoup对象
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    data1 = soup.find(class_='wea')
    weather = data1.text
    data2 = soup.find(class_='tem')
    temps = data2.text
    # find方法获得的是源码，还需要经过text转换
    return temps, weather



# 函数命名时有两个单词组合时，用下划线相连，
# 定义了函数的名字叫send_email()，定义了两个参数tem和weather。当然，等下需要把爬虫获取到的温度信息和天气信息传递给该函数的参数。
def send_email(temps, weather):
    # 发送邮件：1.连接服务器2.通过账号/密码登录邮箱3.填写收件人4.填写主题5.撰写正文6.发送邮件7.退出邮箱
    # 连接服务器
    # 使用smtplib库来连接服务器,smtplib是python的一个内置库，所以不需要用pip安装
    # 把qq邮箱的服务器地址赋值到变量mailhost上，地址需要是字符串的格式,qq邮箱的服务器地址，这个地址是可以通过搜索引擎查到的
    mailhost = 'smtp.qq.com'
    # 实例化一个smtplib模块里的SMTP类的对象，这样就可以使用SMTP对象的方法和属性了
    qqmail = smtplib.SMTP()
    # 连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。调用SMTP对象的connet方法连接服务器
    qqmail.connect(mailhost, 25)
    # 通过账号和密码登录邮箱；填写收件人
    # 调用SMTP对象的login方法登录邮箱
    qqmail.login(account, password)
    # POP3/SMTP服务-授权码-POP3/SMTP服务-nllnfuuutzsibbic，可在第三方客户端登录时，使用SMTP服务登录邮箱时，就可以输入这个授权码作为密码登录
    # 填写主题和撰写正文使用email库
    # 引入了email库中的MIMEText模块和Header模块。
    from email.mime.text import MIMEText
    from email.header import Header
    # 请输入你的邮件正文
    content = '亲爱的，今天的天气是：' + temps + weather
    # 实例化一个MIMEText邮件对象，该对象需要写进三个参数，分别是邮件正文，文本格式和编码,构造了一个纯文本邮件了
    message = MIMEText(content, 'plain', 'utf-8')
    # 用input()获取邮件主题-input('请输入你邮件主题：')
    subject = '今日天气预报'
    # 实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
    # 根据类里面的【属性名】取到【属性】,据MIMEText类里面的Subject的属性名取到该属性,类似根据字典里的【键】取到对应的【值】
    # 不是每一个类都可以这样访问其属性的，之所以能这样访问是因为这个MIMEText的类实现了这个功能
    # message['Subject'] = Header(subject, 'utf-8') 就是在为message['Subject']这个属性赋值
    message['Subject'] = Header(subject, 'utf-8')
    try:
        # 发送邮件和退出邮箱
        # 发送邮件，调用了sendmail()方法，写入三个参数，分别是发件人，收件人，和字符串格式的正文
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
        # 退出邮箱,sendmail()发送邮件，括号里面有三个参数，
        # 第0个是发件人的邮箱地址，第1个是收件人的邮箱地址，第2个是正文，但必须是字符串格式，所以用as_string()函数转换了一下
    except:
        print('邮件发送失败')
    qqmail.quit()


# 实现定时功能，Python有两个内置的标准库——time和datetime
# 定义一个函数叫job()；42行是打印'开始一次任务'，为了记录和显示任务的开始。
# 是调用爬虫函数weather_spider()，然后把这个函数内部return的
# 两个变量tem、weather赋值给job()函数里面的变量temps，weather；第44行是调用函数send_email()，并且把参数传入。
def job():
    print('开始一次任务')
    temps, weather = weather_spider()
    send_email(temps, weather)
    print('任务完成')
    
schedule.every().day.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)