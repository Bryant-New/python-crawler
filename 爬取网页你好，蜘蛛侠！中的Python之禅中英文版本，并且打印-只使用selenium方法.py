#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ��ϰʹ��selenium��ȡ��̬��ҳ����Ϣ����ϰselenium��BeautifulSoup�Ĵ���ʹ��
# selenium��ʹ��˵����https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

# ������Ҫʹ�õĿ⺯��
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # ����Optionģ��
from selenium.webdriver.chrome.webdriver import RemoteWebDriver  # ��selenium���е���RemoteWebDriverģ��

# ��ã�֩��������һ����̬��ҳ��URL��https://localprod.pandateacher.com/python-manuscript/hello-spiderman/
# Python֮��������û�д�����ҳԴ�����У��޷�ͨ��requests.get()��BeautifulSoup��ȡ��Python֮���������ݣ����������ǿ���ͨ��selenium��ȡ��
# 1.ʹ��selenium��ȡ��ҳ2.����ϲ������ʦ������3.��ȡelements����Ⱦ���������ҳԴ�������Ӣ�Ķ���
# �������������
driver = webdriver.Chrome()
# ʹ��ʵ����������������ȡĿ����ҳ
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# ��ͣ2min
time.sleep(2)

# ��λ������������ϲ������ʦ������������λ�ö�ӦhtmlԴ���룬id��teacher
teacher = driver.find_element_by_id('teacher')
# ģ������:ϲ������ʦ���֣����
teacher.send_keys('���')
# ��λ������������ϲ�������̡�����������λ�ö�ӦhtmlԴ���룬id��assistant
assistant = driver.find_element_by_id('assistant')
# ģ������:ϲ�����������֣�����
assistant.send_keys('����')
# ��λ���ύ-��ťλ�ö�ӦhtmlԴ���룬class��subͨ��class name��λԪ��
button = driver.find_element_by_class_name('sub')
# ������ύ����ť
button.click()
time.sleep(1)

# ��λ��Python֮��λ�ö�ӦhtmlԴ���룬class��contentͨ��class name��λԪ��
contents = driver.find_elements_by_class_name('content')
# ��ȡ����
for content in contents:
    # ʹ��h1��ǩ����ȡ����-������find_element_by_tag_name.text
    title = content.find_element_by_tag_name('h1').text
    # ,ʹ��p��ǩ����ȡ����-������find_element_by_tag_name.text
    chan = content.find_element_by_tag_name('p').text
    print(title+'\n'+chan+'\n')
driver.close()