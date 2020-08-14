#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ʵ�ֹ��ܣ����ǽ����һ��������ʶ����ص����������������ʻ㡢���ӡ����»���䣬�᷵������Ĵʻ㡣
# �������Ե���վnlpir����http://ictclas.nlpir.org/nlpir/
import requests
import json

# ��Word2vec��������ʻ㣩����һ���ϴ����ݣ�Ȼ��������������ݣ����ظ����ǵĹ��̡�����������д����ҳԴ����HTML���������Ҫ�鿴Network����XHR��
# �򿪼�鹤�ߣ�ѡ��Network-XHR����Ȼ���ı������롰���־硱��Ȼ����һ�Ρ�Word2vec���Ĺ���
# ���Headersȷ��XHR�������ַ��ʲô�������������ʲô����Preview��Ԥ�������У���ѯ���ص�����ʻ�
# ��0���򣬸��������������ַ�ǣ�http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do���Լ�����ķ�ʽPOST��
# ��1������������Ϥ��User-Agent������������������Ϣ�ж��ύ��������˻������棬����Ҫ��װheaders����������αװ�������
# ��2���򣬾���POST�������ύ�����ݡ��㿴������һ���ֵ�Ľṹ������һ��������content���Ͷ�Ӧ��ֵ�������־硣
# �ύ��Щ���ݸ����������������᷵�ظ�����һ���ֵ䣬�������Preview�п���
# ��װheaders��ģ�����������վ�������ύ����
headers={
    'Origin': 'http://ictclas.nlpir.org',
    'Referer': 'http://ictclas.nlpir.org/nlpir/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.105 Safari/537.36'
}
# Headers�е�requests��url
url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
# ��ȡ��Ҫ�������ı�
words = input('����������Ҫ��ѯ�Ĵʻ�:')
# ��װ�������ݣ�������Headers����еĵײ��������͵�����������һ���ֵ䡣
data = {'content': words}
# ����post����
res = requests.post(url, headers=headers, data=data)
# res��һ��html����-�޷���ʾ�������ݣ���Ҫʹ��.text�ַ�������ʾ����
# res.text��resתΪjson��ʽ���ַ���
data = res.text
# ����post����������õ��˷��ص����ݽ����res.text��һ��json��ʽ���ַ�����
# ����ֻȡ����Ҫ������ʻ�������ϵ��������ҳ�еĴʻ㣬�������ϵ���ֵ
# �����json����ת�����ֵ䣬�ٸ��ݼ���ȡֵ��Ҫ�õ�json.loads(),ʹ��loads()��������json��ʽ���ַ���תΪ�ֵ�
data1 = json.loads(data)
# ��ӡ����
print('�͡�'+words+'����صĴʻ㣬���ٻ��У�')
# forѭ�������б�
f = 0
# str�����֣�-�������֣�str(9)-9
for i in data1['w2vlist']:
    f = f+1
    #  ָ���ָ����Ƕ��ţ�ÿ����һ�����ţ�����һ�¡�
    word = i.split(',')
    print('('+str(f)+')'+word[0]+'������ض�Ϊ'+word[1])  # ��ӡ����
    print(str(f))