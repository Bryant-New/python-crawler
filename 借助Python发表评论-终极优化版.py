#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
import requests
import json

session = requests.session()
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}



# ��������
# ��ȡcookies
def cookies_read():
    cookies_txt = open('cookies.txt', 'r')
    cookies_dict = json.load(cookies_txt.read())
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return cookies


# ��¼
def sign_in():
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    data = {
        'log': input('����������˺�'),
        'pwd': input('�������������'),
        'wp-submit': '��¼',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
        'testcookie': '1'
    }
    # cookies�洢
    session.post(url, headers=headers, data=data)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    f = open('cookies.txt','w')
    f.write(cookies_str)
    f.close()


def write_message():
    url_2 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_2 ={
        'comment': input('��������Ҫ��������ۣ�'),
        'submit': '��������',
        'comment_post_ID': '13',
        'comment_parent': '0'
    }
    return session.post(url_2, headers=headers, data=data_2)

try:
    session.cookies = cookies_read()
except FileNotFoundError:
    sign_in()

num = write_message()
if num.status_code == 200:
    print('�ɹ���')
else:
    sign_in()
    num = write_message()