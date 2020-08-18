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
import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

account = input("�������������:")
password = input("�������������:")
receiver = input('�������ռ��˵����䣺')


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
    
        ���: %s
        ����: %s
        ����: %s
        ԭ��: %s
         '''%(num, name, url, ingredients)
        list_all = list_all+food_info
    return list_all


def send_email(list_all):
    global account, password, receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(account, password)
    content = '�װ��ģ����ܵ����Ų������£�'+list_all
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '��ĩ�Ը�ɶ'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('�ʼ����ͳɹ�')
    except:
        print('�����ʼ�ʧ��')


def job():
    print('��ʼһ������')
    list_all = recipe_spider()
    send_email(list_all)
    print('�������')


schedule.every().friday.at("18:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
