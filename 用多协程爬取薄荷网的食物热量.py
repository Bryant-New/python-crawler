#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# ѡ��һ���д洢ʳ��������Ϣ����վ�����������ݣ�������������һ������������йأ��ҿ��Բ�ѯʳ�����ݵ���վ
# ����Ŀ���̣�1.��ȷĿ��2.��������3.����ʵ��
# �ж����ݴ���������ж������Ƿ����html�У��Ǵ���html�У�������HTML�У��鿴XHR���Ķ�XHR��name������ÿ��XHR
# ���һ��򿪡���顱���ߣ������Network��Ȼ��ˢ��ҳ�档�����0������1����Response������Response���ҵ�ʳ�����Ϣ��˵��������Ҫ�����ݴ���HTML��
# ��0������1��Headers�����Է��ֱ���������ҳ����ʽ��get��֪��������ʽ��get�����Ǿ�֪��������requests.get()��ȡ����
# ǰ10������ʳ��������ַ���ǣ�http://www.boohee.com/food/group/+����
# ÿ��ʳ�����+ÿһҳʳ���¼��ַ��http://www.boohee.com/food/view_menu?page=ҳ����ֻҪ�ı�page��������֣�����ʵ�ַ�ҳ
# ��������ʳ�����������ݶ�����HTML��Ϳ�����BeautifulSoupģ��������
# �һ��򿪡���顱���ߣ���Elements�������꣬������Ƶ�ʳ�Easy Fun ����Ӫ���ࡿ����ᷢ����<li class="item clearfix">Ԫ���£�
# ����ʳ�����Ϣ������ʳ����������ӡ�ʳ����������,���href="/shiwu/fdd9b123"���ͻ���ת����Easy Fun ����Ӫ���ࡿ������ҳ��
# �����Ϣ����html��ҳ�У���network�в鿴XHR����Ϣ�洢��XHR�У���鷢������ʽ��post�Ļ�����ʹ��request.post�������
# ÿ��ʳ�����Ϣ�����ֱ������һ��<li class="item clearfix">��</li>��ǩ�ÿҳʳ���¼����10��ʳ�
# �պö�Ӧ����ҳԴ�������10��<li class="item clearfix">��</li>��ǩ��
# ��find_all/find������ȡ��<li class="item clearfix">��</li>��ǩ�µ�ʳ���������ӡ����ƺ�������
# ��ȡ�����ݣ����Ǵ�csv��openpyxlģ��������ѡ��ʹ������һ��ģ�飬�����ݴ洢����
# 1.��ȡ���ݣ�request.get2.�������ݣ�BeautifulSoup 3.��ȡ���ݣ�find_all 4.�洢���ݣ�csv/oepnpyxl
# ������Ҫ�Ŀ��ģ��


from gevent import monkey
monkey.patch_all()
# �ó������첽ģʽ
import gevent,requests, bs4, csv
from gevent.queue import Queue
# ��������ģ�飬������ǰ������ó�����ַ���ɣ�
# ��forѭ�������ǰ3������ʳ������ǰ3ҳʳ���¼����ַ��
# ��11������ʳ������ǰ3ҳʳ���¼����ַ��������Щ��ַ�Ž����У���ӡ����

# �������ж���,����ֵ��work
work = Queue()
# ǰ��������ʳ������ǰ��ҳ��ʳ���¼��ַ��
url_1 = 'https://www.boohee.com/food/group/{type}?page={page}'
# ͨ������forѭ�������÷�������ֺ�ҳ��������
# �ѹ���õ���ַ��put_nowait������ӽ�������
for x in range(1, 4):
    for y in range(1, 4):
        real_url = url_1.format(type=x, page=y)
        work.put_nowait(real_url)

print(work)



