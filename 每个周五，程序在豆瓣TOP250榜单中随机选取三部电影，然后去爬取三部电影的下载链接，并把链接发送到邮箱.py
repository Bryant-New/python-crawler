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
import requests, csv, random, smtplib, schedule, time
from bs4 import BeautifulSoup
from urllib.request import quote
from email.mime.text import MIMEText
from email.header import Header


import requests, csv, random, smtplib, schedule, time
from bs4 import BeautifulSoup
from urllib.request import quote
from email.mime.text import MIMEText
from email.header import Header


# 第一部分：爬取豆瓣电影
def get_movielist():
    csv_file=open('movieTop.csv', 'w', newline='',encoding='utf-8')
    writer = csv.writer(csv_file)
    for x in range(10):
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
        res = requests.get(url,headers=headers)
        bs = BeautifulSoup(res.text, 'html.parser')
        bs = bs.find('ol', class_="grid_view")
        for titles in bs.find_all('li'):
            title = titles.find('span', class_="title").text
            list1 = [title]
            writer.writerow(list1)
    csv_file.close()


# 第二部分：在阳光电影网站爬取电影链接
def get_randommovie():
    movielist=[]
    csv_file=open('movieTop.csv','r',newline='',encoding='utf-8')
    reader=csv.reader(csv_file)
    for row in reader:
        movielist.append(row[0])
    three_movies=random.sample(movielist,3)
    contents=''
    for movie in three_movies:
        gbkmovie = movie.encode('gbk')
        headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        urlsearch = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(gbkmovie)
        res = requests.get(urlsearch,headers=headers)
        res.encoding='gbk'
        soup_movie = BeautifulSoup(res.text,'html.parser')
        urlpart=soup_movie.find(class_="co_content8").find_all('table')
        if urlpart:
            urlpart=urlpart[0].find('a')['href']
            urlmovie='https://www.ygdy8.com/'+urlpart
            res1=requests.get(urlmovie)
            res1.encoding='gbk'
            soup_movie1=BeautifulSoup(res1.text,'html.parser')
            urldownload=soup_movie1.find('div',id="Zoom").find('span').find('table').find('a')['href']
            content=movie+'\n'+urldownload+'\n\n'
            print(content)
            contents=contents+content
        else:
            content='没有'+movie+'的下载链接'
            print(content)
    return contents


# 第三部分：将获取的链接发送邮件
def send_movielink(contents):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    account = '×××××××××@qq.com' # 因为是自己发给自己，所以邮箱账号、密码都可以提前设置好，当然，也可以发给别人啦
    password = '×××××××××××××××' # 因为是自己发给自己，所以邮箱账号、密码都可以提前设置好，当然，也可以发给别人啦。
    qqmail.login(account,password)
    receiver='×××××××××@qq.com'  # 因为是自己发给自己，所以邮箱账号、密码都可以提前设置好，当然，也可以发给别人啦。
    message = MIMEText(contents, 'plain', 'utf-8')
    subject = '电影链接'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()


# 第四部分：主函数，掉用其他函数执行
def job():
    get_movielist()
    contents=get_randommovie()
    send_movielink(contents)


schedule.every().friday.at("18:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
