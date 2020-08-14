#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ʵ�ֹ��ܣ�����ͼ������˹���http://www.tuling123.com/�Ľӿڣ�����һ����������Ļ�����
# ��ȡ������ͼ������˹���http://www.tuling123.com/�Ľӿڣ�
import requests
import json

# ����post���������json���ݣ���ָ���Ľӿڷ���post����
# 654261�����滻���κγ���С��32���ַ���Ŷ
userid = str(654261)
# ��¼apikey
apikey = str('6df12564ffb447969e0e13e6f7c3f3e6')


# ����post����
def robot(content):
    # ͼ��api
    # ��r��ʾ�����ַ���,r�Ǳ����ַ���ԭʼֵ����˼,��Ϊwindows�µ�Ŀ¼�ַ�����ͨ����б��"\",��б����Python���ַ�������ת�������
    # ��r����Ϊ�˱���������������鿴apiʹ���ĵ�����������ֻ��Perception��useinfo�Ǳ������
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # ����post�ύ����
    data = {
        "perception": {
            "inputText": {
                "text": content
            }
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": userid,
        }
    }
    # ת��Ϊjson��ʽ�����ַ�����ʽ���ֵ䣩
    jsondata = json.dumps(data)
    # ����post����
    response = requests.post(api, data=jsondata)
    # �����ص�json���ݽ���
    robot_res = json.loads(response.content)
    # ��ȡ�Ի�����
    print(robot_res["results"][0]['values']['text'])


for x in range(10):
    content = input("talk:")
    # ����Ի�����
    robot(content)
    if x == 10:
        break
    # ʮ��֮��ͽ����Ի������ֿ��Ը�Ŷ�����뼸�ξͼ���


while True:
    content = input("talk:")
    # ����Ի�����
    robot(content)
    if content == 'bye':
        break
# �����Ի���ѭ��
while True:
    # ����Ի�����
    content = input("talk:")
    robot(content)