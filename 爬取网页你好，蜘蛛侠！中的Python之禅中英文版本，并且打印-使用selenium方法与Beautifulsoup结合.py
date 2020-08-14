#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ��ϰʹ��selenium��ȡ��̬��ҳ����Ϣ����ϰselenium��BeautifulSoup�Ĵ���ʹ��
# selenium��ʹ��˵����https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

# ������Ҫʹ�õĿ⺯��
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# ��ã�֩��������һ����̬��ҳ��URL��https://localprod.pandateacher.com/python-manuscript/hello-spiderman/
# Python֮��������û�д�����ҳԴ�����У��޷�ͨ��requests.get()��BeautifulSoup��ȡ��Python֮���������ݣ����������ǿ���ͨ��selenium��ȡ��
# 1.ʹ��selenium��ȡ��ҳ2.����ϲ������ʦ������3.��ȡelements����Ⱦ���������ҳԴ�������Ӣ�Ķ���
# ����`selenium`��ȡ����Ⱦ��ɵ�`Elements`�е���ҳԴ���룬Ȼ��`BeautifulSoup`�ǳ���������ȡ���ݡ�
# �������������
driver = webdriver.Chrome()
# ʹ��ʵ����������������ȡĿ����ҳ
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# ��ͣ���룬�ȴ����������
time.sleep(2)
teacher = driver.find_element_by_id('teacher')  # ��λ������������ϲ������ʦ������������λ��
teacher.send_keys('���������ѽ') # ��������
assistant = driver.find_element_by_name('assistant')  # ��λ������������ϲ�������̡�����������λ��
assistant.send_keys('��ϲ��') # ��������
button = driver.find_element_by_class_name('sub')  # ��λ�����ύ����ť
button.click()  # ������ύ����ť
time.sleep(1)  # �ȴ�һ��
# ʹ��selenium��page_source��������ֱ�ӷ���ҳ��Դ��
pageSourece = driver.page_source
# ʹ��bs������ҳ
soup = BeautifulSoup(pageSourece, 'html.parser')
# �ҵ�Դ����Python֮�����İ��Ӣ�İ����ڵ�Ԫ��class=content
contents = soup.find_all(class_="content")
for content in contents:  # �����б�
    title = content.find('h1').text  #  ��ȡ����
    chan = content.find('p').text.replace(' ', '')  # ��ȡPython֮�������ģ�����ȥ������ǰ������пո�
    print(title + chan + '\n')  # ��ӡPython֮���ı���������
driver.close()