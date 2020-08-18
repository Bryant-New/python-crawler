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
# ������Ҫʹ�õĿ⺯��
import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time

# ����account��password��receiverΪȫ�ֱ���������input()��ȡ��������
# ��ȡ�����˺�
account = input('������������䣺')
# ��ȡ��������
password = input('������������룺')
# ��ȡ�ռ��˵�����
receiver = input('�������ռ��˵����䣺')


# ���д��룬�����װ�ɺ���������ʹ��
def weather_spider():
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    # ѡ��������ڵ�����������ַ���滻��δ����е�URL��General�е�url,htmlԴ���ж�Ӧ�ĵ�0������
    url = 'http://www.weather.com.cn/weather/101310101.shtml'
    res = requests.get(url, headers=headers)
    # ԭ��ҳ����utf-8��ʽ����ģ�resĬ������AscII����룬��Ҫ�������룬����Ҫ��encoding��佫���뷽ʽ����ת��
    res.encoding = 'utf-8'
    print(res.status_code)
    # ��ӡ���󷵻ص�html��ҳԴ����-res.text
    # print(res.text)
    # ʹ��Beautifulsoup��ȡ�ͽ�������
    # ����ҳ����ΪBeautifulSoup����
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    data1 = soup.find(class_='wea')
    weather = data1.text
    data2 = soup.find(class_='tem')
    temps = data2.text
    # find������õ���Դ�룬����Ҫ����textת��
    return temps, weather



# ��������ʱ�������������ʱ�����»���������
# �����˺��������ֽ�send_email()����������������tem��weather����Ȼ��������Ҫ�������ȡ�����¶���Ϣ��������Ϣ���ݸ��ú����Ĳ�����
def send_email(temps, weather):
    # �����ʼ���1.���ӷ�����2.ͨ���˺�/�����¼����3.��д�ռ���4.��д����5.׫д����6.�����ʼ�7.�˳�����
    # ���ӷ�����
    # ʹ��smtplib�������ӷ�����,smtplib��python��һ�����ÿ⣬���Բ���Ҫ��pip��װ
    # ��qq����ķ�������ַ��ֵ������mailhost�ϣ���ַ��Ҫ���ַ����ĸ�ʽ,qq����ķ�������ַ�������ַ�ǿ���ͨ����������鵽��
    mailhost = 'smtp.qq.com'
    # ʵ����һ��smtplibģ�����SMTP��Ķ��������Ϳ���ʹ��SMTP����ķ�����������
    qqmail = smtplib.SMTP()
    # ���ӷ���������һ�������Ƿ�������ַ���ڶ���������SMTP�˿ںš�����SMTP�����connet�������ӷ�����
    qqmail.connect(mailhost, 25)
    # ͨ���˺ź������¼���䣻��д�ռ���
    # ����SMTP�����login������¼����
    qqmail.login(account, password)
    # POP3/SMTP����-��Ȩ��-POP3/SMTP����-nllnfuuutzsibbic�����ڵ������ͻ��˵�¼ʱ��ʹ��SMTP�����¼����ʱ���Ϳ������������Ȩ����Ϊ�����¼
    # ��д�����׫д����ʹ��email��
    # ������email���е�MIMETextģ���Headerģ�顣
    from email.mime.text import MIMEText
    from email.header import Header
    # ����������ʼ�����
    content = '�װ��ģ�����������ǣ�' + temps + weather
    # ʵ����һ��MIMEText�ʼ����󣬸ö�����Ҫд�������������ֱ����ʼ����ģ��ı���ʽ�ͱ���,������һ�����ı��ʼ���
    message = MIMEText(content, 'plain', 'utf-8')
    # ��input()��ȡ�ʼ�����-input('���������ʼ����⣺')
    subject = '��������Ԥ��'
    # ʵ������һ��Header�ʼ�ͷ���󣬸ö�����Ҫд�������������ֱ����ʼ�����ͱ��룬Ȼ��ֵ���Ⱥ���ߵı���message['Subject']��
    # ����������ġ���������ȡ�������ԡ�,��MIMEText�������Subject��������ȡ��������,���Ƹ����ֵ���ġ�����ȡ����Ӧ�ġ�ֵ��
    # ����ÿһ���඼�����������������Եģ�֮������������������Ϊ���MIMEText����ʵ�����������
    # message['Subject'] = Header(subject, 'utf-8') ������Ϊmessage['Subject']������Ը�ֵ
    message['Subject'] = Header(subject, 'utf-8')
    try:
        # �����ʼ����˳�����
        # �����ʼ���������sendmail()������д�������������ֱ��Ƿ����ˣ��ռ��ˣ����ַ�����ʽ������
        qqmail.sendmail(account, receiver, message.as_string())
        print('�ʼ����ͳɹ�')
        # �˳�����,sendmail()�����ʼ�����������������������
        # ��0���Ƿ����˵������ַ����1�����ռ��˵������ַ����2�������ģ����������ַ�����ʽ��������as_string()����ת����һ��
    except:
        print('�ʼ�����ʧ��')
    qqmail.quit()


# ʵ�ֶ�ʱ���ܣ�Python���������õı�׼�⡪��time��datetime
# ����һ��������job()��42���Ǵ�ӡ'��ʼһ������'��Ϊ�˼�¼����ʾ����Ŀ�ʼ��
# �ǵ������溯��weather_spider()��Ȼ�����������ڲ�return��
# ��������tem��weather��ֵ��job()��������ı���temps��weather����44���ǵ��ú���send_email()�����ҰѲ������롣
def job():
    print('��ʼһ������')
    temps, weather = weather_spider()
    send_email(temps, weather)
    print('�������')
    
schedule.every().day.at("07:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)