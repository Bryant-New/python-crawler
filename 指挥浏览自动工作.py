#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ����������֤��ܸ��ӵ���վʱ��selenium��������ȥ�ֶ�������֤�룬Ȼ���ʣ�µĲ�������������
# selenium-ǿ���Python�⡣�ü��д��룬����������������Զ��򿪡����롢����Ȳ�������������һ���������û��ڲ���һ����
# ��Щ�������ӡ����ܸ��ӵ���վ��selenium����򻯣�����̬��ҳ������̬��ҳһ���򵥡�
# ��̬��ҳ-htmlд������ҳ��ʹ��ʹ��BeautifulSoup��ȡ��������ҳ����ҳԴ�����оͰ�������ҳ��������Ϣ����ҳ��ַ����URL������ҳԴ�����URL
# ��̬��ҳ-HTMLԴ��������Ⱦ��ɵ�ElementsԴ����һ������̬��ҳ����QQ���֣���ȡ�����ݲ���HTMLԴ�����У�������json�У���ֱ��ʹ����ַ����URL
# ��̬��ҳ-��Ҫ�ҵ�json���ݵ���ʵURL���е�����û�д���HTMLԴ���У�URL�����߼����ӵ����ʱ��selenium���������ó�����������ʵ�ش�һ���������
# ��̬��ҳ-����ҳ���Ϸ�����תʱ����Ӧ��ҳ��ַ���е���ҳû�б仯����Ϊ��̬��ҳ
# �ȴ��������ݶ����ص�Elements��֮���ٰ������ҳ������̬��ҳ��ȡ�ͺ��ˡ��ٶȽ���
# ���عȸ���������÷���
# #��selenium���е���webdriverģ��
from selenium import webdriver
import time

# selenium��λ�ȡ����������ȡ����
# ��������ΪChrome����ʵ�ش�һ��Chrome���������Chrome���������Ϊ���棬Ȼ��ֵ������driver��driver��ʵ�����������
driver = webdriver.Chrome()
# ʹ��selenium��ȡ���ݣ�get(URL)��webdriver��һ������������ʹ����Ϊ���ָ��URL����ҳ��
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
# �ȴ�2�룬��������������������ҳ��Ҫ�ķ�һЩʱ�䣬
time.sleep(2)

# ��������-selenium��������ȡ�ģ���Elements�е��������ݣ���BeautifulSoup����������ֻ��Network�е�0���������Ӧ��
# ʹ��BeautifulSoup������ȡ����ʱ������Ҫ��Response�������ΪBeautifulSoup����Ȼ���ٴ�����ȡ���ݡ�
# ��selenium����ҳ�򿪣�������Ϣ�Ͷ����ص���Elements���֮�󣬾Ϳ��԰Ѷ�̬��ҳ�þ�̬��ҳ�ķ�����ȡ�ˡ�
# ��selenium�У���ȡ������ҳ������driver�У����󣬽�������ȡ��ͬʱ���ģ�������driver���ʵ�������������ɡ�
# �ҵ�����������ϲ������ʦ������������λ��
teacher = driver.find_element_by_id('teacher')

# ��ȡ������������WebElement��������ֱ�Ӵ�ӡ�������ص���һ��������������
# WebElement�������Tag�������ƣ���Ҳ��һ������������ͨ����������ȡ���Ե�ֵ�����������.get_attribute()��
# ��ȡurl-ת���ַ���-��� WebElement����-��ת���ַ���
# ��ȡ���Ԫ�صķ���-find_element_by_��BeautifulSoup�е�find���ƣ�������ȡ����ҳ�е�һ������Ҫ���Ԫ��
# .send_keys() # ģ�ⰴ�����룬�Զ���д��
teacher.send_keys('���������ѽ')  # ��������
assistant = driver.find_element_by_name('assistant')  # �ҵ�����������ϲ�������̡�����������λ��
assistant.send_keys('��ϲ��')  # ��������
time.sleep(2)
button = driver.find_element_by_class_name('sub')  # �ҵ����ύ����ť
time.sleep(1)
# ���Ԫ��
button.click()  # ������ύ����ť
time.sleep(1)
# driver.close()�ǹر������������ÿ�ε�����webdriver֮�󣬶�Ҫ��������֮�����һ��driver.close()�����ر���
# ʹ��selenium�����������֮��ҲҪ�ǵùر������
driver.close()

