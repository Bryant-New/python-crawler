#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
import requests
import openpyxl

# Excel�ļ�д�룺1.����������2.��ȡ������3.������Ԫ��4.���湤����
# ����������
wb = openpyxl.Workbook()
# ��ȡ�������Ļ��
sheet = wb.active
# ������������
sheet.title = 'song'
# ��excel������ӱ�ͷ��������������ר��������ʱ���Ͳ�������
# �ֱ���A1��B1��C1��D1��Ԫ����д�롰����������������ר������������ʱ�����͡��������ӡ���
sheet['A1'] = '������'  # �ӱ�ͷ����A1��Ԫ��ֵ
sheet['B1'] = '����ר��'  # �ӱ�ͷ����B1��Ԫ��ֵ
sheet['C1'] = '����ʱ��'  # �ӱ�ͷ����C1��Ԫ��ֵ
sheet['D1'] = '��������'  # �ӱ�ͷ����D1��Ԫ��ֵ

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# ��python����ģ���������ķ�������,��������ʲô�豸��ʲô���������
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
for x in range(5):
    # ��������װΪ�ֵ�
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'txt.yqq.song',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '�ܽ���',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # ����get��������������б�--��ȡ����
    res_music = requests.get(url, params=params, headers=headers)
    # ʹ��json()��������response����תΪ�б�/�ֵ�-��������
    json_music = res_music.json()
    # һ��һ���ȡ�ֵ䣬��ȡ�赥�б�-��ȡ����
    list_music = json_music['data']['song']['list']

    # list_music��һ���б�music���������Ԫ��
    for music in list_music:
        # ��nameΪ�������Ҹ��������Ѹ�������ֵ��name
        name = music['name']
        # ����ר��������ר��������album
        album = music['album']['name']
        # ���Ҳ���ʱ������ʱ����ֵ��time
        time = music['interval']
        # ���Ҳ������ӣ������Ӹ�ֵ��link
        link = 'https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html\n\n'
        # ��name��album��time��linkд���б���append��������д��Excel
        sheet.append([name, album, time, link])
        print('��������' + name + '\n' + '����ר��:' + album + '\n' + '����ʱ��:' + str(time) + '\n' + '��������:' + link)

# ��󱣴沢�������Excel�ļ�
wb.save('Jay.xlsx')


