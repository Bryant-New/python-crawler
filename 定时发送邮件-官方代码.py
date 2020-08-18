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
import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input('������������䣺')
password = input('������������룺')
receiver = input('�������ռ��˵����䣺')

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    tem=tem1.text
    weather=weather1.text
    return tem,weather

def send_email(tem,weather):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost,25)
    qqmail.login(account,password)
    content= tem+weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '��������Ԥ��'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('�ʼ����ͳɹ�')
    except:
        print ('�ʼ�����ʧ��')
    qqmail.quit()

def job():
    print('��ʼһ������')
    tem,weather = weather_spider()
    send_email(tem,weather)
    print('�������')

schedule.every().day.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
# ������������䣺874089278@qq.com
# ������������룺nllnfuuutzsibbic
# �������ռ��˵����䣺18811316839@163.com
# ���������Զ�˷�����