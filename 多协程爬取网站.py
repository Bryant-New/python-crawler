#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# ���Ը��������趨��ʱ���Զ���ȡ���ݣ��ڶ���֪ͨ���ܣ���������԰���ȡ�������ݽ�����ʼ�����ʽ�Զ����͵����ǵ����䡣
# �Զ���ȡÿ�յ�����������ʱ���������ݺʹ�����ʾ���͵��������

from gevent import monkey
# ��gevent���ֵ���monkeyģ��
monkey.patch_all()
# monkey.patch_all()�ܰѳ�����Э��ʽ���У���������ʵ���첽
import gevent, time, requests
# ����gevent��time��requests
from gevent.queue import Queue
# ��gevent���е���quueģ��


start = time.time()

url_list = [
'https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/'
]

work = Queue()
# ��Queue()�ܴ���queue�����൱�ڴ�����һ�������κδ洢�����Ŀն���
for url in url_list:
# ����url_list
    work.put_nowait(url)
    # ��put_nowait()������������queue��������Ǿ��ܵ�����������put_nowait�����������ǵ�ÿ����ַ���洢�����Ǹոս����õĿն�����


def crawler():
    while not work.empty():
    # �����в��ǿյ�ʱ�򣬾�ִ������ĳ���
        url = work.get_nowait()
        # ��get_nowait()�������԰Ѷ��������ַȡ����
        r = requests.get(url)
        # ��requests.get()����ץȡ��ַ��
        print(url, work.qsize(), r.status_code)
        # ��ӡ��ַ�����г��ȡ�ץȡ�����״̬�롣


tasks_list = [ ]
# �����յ������б�
for x in range(2):
# �൱�ڴ�����2������
    task = gevent.spawn(crawler)
    # ��gevent.spawn()����ִ��crawler()����������
    tasks_list.append(task)
    # �������б����������
gevent.joinall(tasks_list)
# ��gevent.joinall������ִ�������б�����������񣬾��������濪ʼ��ȡ��վ
end = time.time()
print(end-start)