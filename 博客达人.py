#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ʹ��seleniumʵ�ֿ��ӻ�����������ķ�����1.��ȡ��ҳ2.�����û����������¼3.������±��⣬������������������
# ʹ��selenium��ȡ���ݣ�����Ԫ��

# ������Ҫʹ�õĿ⺯��
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import RemoteWebDriver

# ��ȡ�û��������������
while True:
    comment_content = input('����������Ҫ�����۵����ݣ����س��ύ��')
    if comment_content == '':
        print('&'*5, '�������ݲ�����Ϊ��', '&'*5)
    else:
        break
# ����һ��ʹ���Լ������ϵ������
# ʵ�������������
driver = webdriver.Chrome()
# ��ȡ��ҳ
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
# ͣ��2��
time.sleep(2)
# ��λ���û�������������û�����ʹ��id��user_login��λ���û������
login_name = driver.find_element_by_id('user_login')
# ģ�ⰴ�������û���spiderman���Զ���д��
login_name.send_keys('spiderman')
# ͣ��1��
time.sleep(1)
# ��λ������������������룬ʹ��id��user_pass��λ�����������
password = driver.find_element_by_id('user_pass')
# ģ�ⰴ����������crawler334566���Զ���д��
password.send_keys('crawler334566')
# ��λ��¼��ť��ʹ��id��wp-submit��λ����¼��
submit_btn = driver.find_element_by_id('wp-submit')
# ģ������¼loginԪ��
submit_btn.click()
# ͣ��2��
time.sleep(2)
# ͨ�����ӵĲ����ı���λ��'��δ����������������ͬ��������㡷'��ƪ����
# ��ȡ�����¶�Ӧ��a��ǩ���������������ҳ��Ѱ��id�����Ƕ�Ӧ��class
# ʹ�������ı���δ����������������ͬ��������㣬��ȡ��Ӧ���µĳ�����
article_link = driver.find_element_by_link_text('δ����������������ͬ���������')
# ģ������ȡ��������ҳ
article_link.click()

# ������������ҳ,��λ����ҳ���±�д���۵��ı�����������-ʹ��id��comment��λ���������ı���
comment_area = driver.find_element_by_id('comment')
# ģ�ⰴ�������������ݣ��Զ���д��
comment_area.send_keys(comment_content)
# ��λ���ύ��ť�������ť�ύ����
comment_submit = driver.find_element_by_id('submit')
# ģ������ť�ύ����
comment_submit.click()

# ���۳ɹ�10s��ر������
time.sleep(10)
driver.close()
print('#' * 6, '���۳ɹ���������ѹر�', '#' * 6)

