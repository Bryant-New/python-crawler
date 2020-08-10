#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
import requests
import json


# ʹ��cookies�����¼״̬������Ҫ�ظ������˺š�����
# ��requests.session()����session�����൱�ڴ�����һ���ض��ĻỰ���������Զ�������cookies��
session = requests.session()
# ��������ƣ���װheader
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# ʹ��Pythonģ�����������վ�����������¼����
# ���йص�¼�Ĳ�����װ���ֵ丳ֵ��data
try:
# ����ܶ���cookies�ļ���ִ�����´��룬����except���룬���õ�¼���ܷ�������
    # ��reader��ȡģʽ������Ϊcookies.txt�ļ�
    cookies_txt = open('cookies.txt', 'r')
    # ����jsonģ���loads���������ַ���ת���ֵ�
    cookies_dict = json.loads(cookies_txt.read())
    # ��ת���ֵ��cookies��ת��cookies�����ĸ�ʽ
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    # ��ȡcookies:����requests����session����cookies����
    session.cookies = cookies
except FileExistsError:
# �����ȡ����cookies�ļ������򱨡�FileNotFoundError(�Ҳ����ļ�)�Ĵ�ִ�����´��룬���µ�¼��ȡ
    # ��¼��ַ
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    # ��¼����
    data = {
        'log': input('�������˺�'),  # д���˻�
        'pwd': input('����������'),  # д������
        'wp-submit': '��¼',  # ��¼��ť
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',  # �ɹ���¼����ת����ַ����ԭ��վ��ַ-������ϰ��վ
        'testcookie': '1'
    }
    # �ڴ�����session����post�����¼���󣬷�������������¼����ַ������ͷ�͵�¼����
    session.post(url, headers=headers, data=data)
    # ��cookiesת�����ֵ�
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookies_dict)
    # ����jsonģ���е�dumps��������cookies���ֵ�ת���ַ���
    cookies_str = json.dumps(cookies_dict)
    print(cookies_str)
    # ������Ϊcookies.txt�ļ�����д��ģʽд������
    f = open('cookies.txt', 'w')
    # ���Ѿ�ת���ַ�����cookiesд���ļ���
    f.write(cookies_str)
    # �ر��ļ�
    f.close()
# ����ҳ�ύ������
# ����200��״̬�룬��ζ�ŷ��������ܵ�����Ӧ�˵�¼���󣬽����˳ɹ���¼
# ��ȡ�����õ�¼��cookie
# ��ȡcookies�ķ���������requests����login_in����cookies���Ի�õ�¼��cookies������ֵ������cookies��
# ��Ҫ���۵�������ַ
url_1 = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# ��ȡ���۲���-���й����۵Ĳ�����װ���ֵ�
data_1 ={
    'comment': input('����������Ҫ��������ۣ�'),
    'submit': '��������',  # �������۵İ�ť
    'comment_post_ID': '13',
    'comment_parent': '0'
}
# ��requests.post���𷢱����۵����󣬷��������������ַ��headers�����۲�����cookies��������ֵ��comment��
# ����cookies�ķ���������post�����д���cookies=cookies�Ĳ�����
comment = session.post(url_1, headers=headers, data=data_1)
print(comment.status_code)
# ���������۵������ص㣺1.post�������������¼2.��õ�¼��cookies3.��cookiesȥ���󷢱�����
# ����session����һ���Ż�cookies
# �����ȡ��cookies�����Զ���¼���������ۣ������ȡ�����������������˺������¼��������
