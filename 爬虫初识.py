# coding=gbk
import requests

res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# �������󣬲��ѷ��صĽ�����ڱ���res��
# ��Reponse����������Զ��������ݵ���ʽ����
pic = res.content
# �½���һ���ļ�ppt.jpg��������ļ�û��·�������ᱻ�����ڳ������еĵ�ǰĿ¼�¡�
# ͼƬ������Ҫ�Զ�����wb��д��
photo = open('ppt.jpg', 'wb')
# ��ȡpic�Ķ���������
photo.write(pic)
# �ر��ļ�
photo.close()
# ͨ����д�ļ���С˵���浽������
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res.encoding = 'utf-8'
novel = res.text
fic = open('���������塷.txt', 'a+')
fic.write(novel)
fic.close()