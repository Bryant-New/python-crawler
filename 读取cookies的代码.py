import json
import requests
# ��reader��ȡģʽ������Ϊcookies.txt���ļ���
cookie_txt = open('cookies.txt', 'r')
# ����jsonģ���loads���������ַ���ת���ֵ�
cookies_dict = json.loads(cookie_txt.read())
# ��ת���ֵ��cookies��ת��cookies�����ĸ�ʽ��
cookies = requests.utils.cookiejar_from_dict(cookies_dict)
# ��ȡcookies�����ǵ���requests����session����cookies���ԡ�
session.cookies = cookies
