#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 实现功能：利用图灵机器人官网http://www.tuling123.com/的接口，创建一个可以聊天的机器人
# 读取官网：图灵机器人官网http://www.tuling123.com/的接口，
import requests
import json

# 创建post请求所需的json数据，向指定的接口发起post请求
# 654261可以替换成任何长度小于32的字符串哦
userid = str(654261)
# 登录apikey
apikey = str('6df12564ffb447969e0e13e6f7c3f3e6')


# 创建post函数
def robot(content):
    # 图灵api
    # 加r表示绝对字符串,r是保持字符串原始值的意思,因为windows下的目录字符串中通常有斜杠"\",而斜杠在Python的字符串中有转义的作用
    # 上r就是为了避免这种情况～，查看api使用文档，发现其中只有Perception和useinfo是必须参数
    api = r'http://openapi.tuling123.com/openapi/api/v2'
    # 创建post提交数据
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
    # 转化为json格式（即字符串形式的字典）
    jsondata = json.dumps(data)
    # 发起post请求
    response = requests.post(api, data=jsondata)
    # 将返回的json数据解码
    robot_res = json.loads(response.content)
    # 提取对话数据
    print(robot_res["results"][0]['values']['text'])


for x in range(10):
    content = input("talk:")
    # 输入对话内容
    robot(content)
    if x == 10:
        break
    # 十次之后就结束对话，数字可以改哦，你想几次就几次


while True:
    content = input("talk:")
    # 输入对话内容
    robot(content)
    if content == 'bye':
        break
# 创建对话死循环
while True:
    # 输入对话内容
    content = input("talk:")
    robot(content)