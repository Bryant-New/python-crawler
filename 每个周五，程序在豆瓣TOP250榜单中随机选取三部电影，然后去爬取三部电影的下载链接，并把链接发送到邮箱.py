#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# ���Ը��������趨��ʱ���Զ���ȡ���ݣ��ڶ���֪ͨ���ܣ���������԰���ȡ�������ݽ�����ʼ�����ʽ�Զ����͵����ǵ����䡣
# �Զ���ȡÿ�յ�����������ʱ���������ݺʹ�����ʾ���͵��������

# �����������ܿ飺1.����2.�ʼ�3.��ʱ
# ����-�ʼ�֪ͨ��ʹ��smtplib��email�⣬��ʱ����-schedule��
# �ٶ�������ַ��http://www.weather.com.cn/weather/101280601.shtml�����"�Ҽ�"����"���"����"Network"��ˢ��ҳ�棬�㿴��0������
# ���ݷ���HTML�û���⡣�����ǵ��Elements���¶����ݷ���<p class="tem">֮�¡���С�ꡱ���ڵ�λ����<p title="С��" class="wea">С��</p>
# ��ҳԴ�������������۲���һ�������ֿ���ʹ��class="wea"��class="tem"��ƥ��Ŀ�����ݣ���ҳԴ���������-��response.encoding���ԣ�
# ����ҳ�ϵ��"�Ҽ�"����"�鿴��ҳԴ����"���ᵯ��һ���µı�ǩҳ��Ȼ������charset���鿴һ�±��뷽ʽ,��ҳ����utf-8����ġ�
# ��response.encodingת��һ�±���

# ����-�ʼ�-��ʱ
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


# ��һ���֣���ȡ�����Ӱ
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


# �ڶ����֣��������Ӱ��վ��ȡ��Ӱ����
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
            content='û��'+movie+'����������'
            print(content)
    return contents


# �������֣�����ȡ�����ӷ����ʼ�
def send_movielink(contents):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    account = '������������������@qq.com' # ��Ϊ���Լ������Լ������������˺š����붼������ǰ���úã���Ȼ��Ҳ���Է���������
    password = '������������������������������' # ��Ϊ���Լ������Լ������������˺š����붼������ǰ���úã���Ȼ��Ҳ���Է�����������
    qqmail.login(account,password)
    receiver='������������������@qq.com'  # ��Ϊ���Լ������Լ������������˺š����붼������ǰ���úã���Ȼ��Ҳ���Է�����������
    message = MIMEText(contents, 'plain', 'utf-8')
    subject = '��Ӱ����'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('�ʼ����ͳɹ�')
    except:
        print ('�ʼ�����ʧ��')
    qqmail.quit()


# ���Ĳ��֣���������������������ִ��
def job():
    get_movielist()
    contents=get_randommovie()
    send_movielink(contents)


schedule.every().friday.at("18:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
