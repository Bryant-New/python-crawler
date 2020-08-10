#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
import requests, bs4
import csv
from bs4 import BeautifulSoup

# ����open()������csv�ļ�������������ļ�����articles.csv����д��ģʽ��w����newline=''
csv_file = open('articles.csv', 'w', newline='', encoding='utf-8')
#  ��csv.writer()��������һ��writer����
writer = csv.writer(csv_file)
# ����һ���б�
list2 = ['����', '����', 'ժҪ']
# ����writer�����writerow()������������csv�ļ���д��һ������ �����⡱�͡����ӡ���"ժҪ"��
writer.writerow(list2)
# ��������ƣ���װheader
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# �Ҽ����HTMLԴ���룬Network�еĵ�0����Ϣ�����±��⣬-���ݴ������ҳ���У�ʹ��Beautifulsoup����������
# ���±����Ӧ��ǩ-<a>,����-target="_blank"��data-za-detail-view-element_name="Title"������target="_blank�������������࣬����׼ȷ��λ�����±��⽫����ȥ
# �����ӱ�ǩ<a>��target����ָʾ�������Ĵ���ת��Ŀ����ҳ��"_blank"����ÿ���һ�γ����Ӵ�һ������
# ��һ������data-za-detail-view-element_name="Title"-�������������⣬����html�﷨�б�׼����������BeautifulSoup���ܲ�ʶ�𣬲��Ƽ�ʹ��
# Ѱ��<a>��ǩ�ĸ���ǩ<h2>��ǩ������������class="ContentItem-title"����׼��λ���±���
# ��ȡ����-requests�⣬��������BeautifulSoup�⣬��ȡ����-��BeautifulSoup�����find_all��������ҳ��۲��һҳ�����һҳ����ַ������дѭ��
# �洢������csv��openpyxlģ��
# ��ҳʹ��params����������ҳ��

url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# ����ƫ����offset����ʼֵΪ��һҳ��ֵ:10
offset = 10

while True:
    # ��װ�����������ö�ҳ����,��Network�е�article?��headers�����query string parameters��Ĳ���
    params = {
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': '10',
        'limit': '10',
        'sort_by': 'voteups',
    }
    # ��ȡ����,�������󣬲�����Ӧ���ݸ�ֵ������res����
    res = requests.get(url, headers=headers, params=params)
    # ȷ�����response����״̬��ȷ
    print(res.status_code)
    # ��ȡ����-���ˢ��ҳ��õ���Ӧ��һҳ�͵ڶ�ҳ�Ĳ�������headers�����query string parameters����
    # ����ֻ��query string parameters�е�offset-ƫ������һ������ҳ���Ӧ��ͨ��ѭ��������ҳ���õ���Ӧҳ���е�����
    # ��������,�������ڶ�̬��ҳ�е����£�һ���ַ�����ҳ�У�һ���ִ���xhr��,ʹ��json()��������response����תΪ�б�/�ֵ�

    # �����Ӧ�ɹ�������
    if int(res.status_code) == 200:
        # ��json��������response����
        articles = res.json()
        print(articles)
        # ��ȡ����
        # ��㶨λ���±���
        # ��ȡ��Ϊdata��ֵ����λ����
        data = articles['data']
        # �����б��õ��б����ÿһ��Ԫ�أ�ÿһ��Ԫ�ض����ֵ䣬ͨ������ֵȡ����
        for i in data:
            # ȡ��������ַ
            # ȡ������ժҪ
            list1 = [i['title'], i['url'], i['excerpt']]
            writer.writerow(list1)
        # ��while ѭ���ڲ�,offset��ֵÿ������20
        offset = offset+20
        if offset>30:
            break
        # ���offset-ƫ��������30����������ҳ��ֹͣ
        # ��������������һ��˼·ʵ�֡�������������������������������
        # �����is_end����Ӧ��ֵ��True���ͽ���whileѭ��
        # if articles['paging']['is_end'] == True:
            #break
        # ��ȡ��ҳ
csv_file.close()
print('ok')
