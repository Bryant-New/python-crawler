# coding: gbk
# python�ڰ�װʱ��Ĭ�ϵı�����ascii���������г��ַ�ascii����ʱ��
# python�Ĵ������ᱨ�����Ĵ�UnicodeDecodeError: 'ascii' codec can't decode byte 0x??
# in position 1: ordinal not in range(128)��pythonû�취�����ascii����ģ���ʱ��Ҫ�Լ����ý�python��Ĭ�ϱ��룬һ������Ϊutf8�ı����ʽ
# strתbytes��encode��bytesתstr��decode,print()�������������ƣ�������ȫ��ӡ���е�unicode�ַ���
# ʹ�ö�Э�̺Ͷ��У���ȡʱ�������Ӿ�TOP100�����ݣ����������ݡ����ݺͼ�飩������csvģ�齫���ݴ洢������
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
from gevent import monkey
monkey.patch_all()
import gevent, requests, bs4, csv
from gevent.queue import Queue


work = Queue()
url_1 = 'http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_1)

url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for x in range(1,11):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)

def crawler():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers, )
        bs_res = bs4.BeautifulSoup(res.text,'html.parser')
        datas = bs_res.find_all('div',class_="mov_con")
        for data in datas:
            TV_title = data.find('a').text
            data = data.find_all('p')
            TV_data =''
            for i in data:
                TV_data =TV_data + ''+ i.text
            writer.writerow([TV_title,TV_data])
            print([TV_title, TV_data])

csv_file = open('���Ӿ�1.txt', 'w', newline='', encoding='utf-8')
# ��Ϊ.csv���Ļ�������룬Ӣ�Ĳ������룬���.txt�ļ���������
writer = csv.writer(csv_file)

task_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)