#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
import requests, bs4
import csv

# �����ļ�-����open����
csv_file = open('����Top250.csv', 'w', newline='')
# ��������-����writer����
writer = csv.writer(csv_file)
#д������-writerow����
writer.writerow(['���', '��Ӱ��', '��������', '�Ƽ���', '����'])

headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# Ѱ�Ҷ���Top250
# ����ȫ��Ŀ���Ӱ�ı�ǩ-<div class='article'>
# ������һ����Ӱȫ����Ϣ�ı�ǩ-<li>..</li>
# �����ڶ�����Ӱȫ����Ϣ�ı�ǩ-<li>..</li>��ÿ����Ӱ��Ϣ��<li>��ǩ���ƣ�article�µ�25��li��ǩ��Ӧ25����Ӱ��Ϣ
# forѭ����10�Σ�1����һҳ
for x in range(10):
    # start=��������ִ�0ÿһҳ��25��ȥ����ʱ��ͨ���ַ�����ƴ�ӾͿ���ʵ����ȡ10ҳurl��Ŀ��
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    # ��25��li��ǩ,��Ӧ25����Ӱ��Ϣ��bs.find_all("li")
    # ��len����print���ҵ���44��li��ǩ����˵����19����Ҫ��li��ǩҲ��ȡ������
    print(len(bs.find_all("li")))
    # ol��ǩ��grid_view���ԣ�����ȷ��ֻ����25���е�Ӱ��Ϣ��li��ǩ
    bs = bs.find('ol', class_="grid_view")
    # forѭ������ÿ��li��ǩ���б�
    for titles in bs.find_all('li'):
        num = titles.find('em', class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span', class_="rating_num").text
        url_movie = titles.find('a')['href']
        if titles.find('span', class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            print(num + '.' + title + '����' + comment + '\n' + '�Ƽ��' + tes +'\n' + url_movie)
        else:
            print(num + '.' + title + '����' + comment + '\n' +'\n' + url_movie)
        writer.writerow([num, title, comment, tes, url_movie])
# ����excel
csv_file.close()


