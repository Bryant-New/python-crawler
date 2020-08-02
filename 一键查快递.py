# 爬取 快递100网站 ，实现输入快递名称和单号就可以查询最新物流状态
# 实现功能：用户输入快递名称和单号，程序即可在快递100https://www.kuaidi100.com/爬取最新物流状态，并将其打印出来。
# 分别调用requests库,负责上传和下载数据。和random库
import requests
import random

cookie = input('请输入网页的cookie值')
kuaidiType = input('请输入快递类型(拼音)')  # input输入的是字符串
kuaidiID = input('请输入快递单号')

url ='https://www.kuaidi100.com/query?'

header = {
    'Accept-Encoding': 'gzip, deflate, br',
    'referer': 'https://www.kuaidi100.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': cookie,
    'Host': 'www.kuaidi100.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
# 调用random库中的random方法
a = random.random()
params ={
        'type': kuaidiType,
        'postid': kuaidiID,
        'temp': str(a),
        'phone': ''
}
# 将要get的内容，以字典的形式记录在params内
r = requests.get(url, params=params, headers=header)
result = r.json()
for i in result['data']:
    print(i['context'])