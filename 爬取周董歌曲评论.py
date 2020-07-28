import requests
# 引用bs4模块
from bs4 import BeautifulSoup

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 循环5次，重复加载并获取
for i in range(5):
    # QQ音乐中对应的周杰伦网址，Network中评论对应的RequestsURL，由字典和列表嵌套形成的XHR数据，格式为.json
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=70363873764404899&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=4&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    # Query String Parameters里的内容，直接复制下来，封装为一个字典，传递给params,复制过来的参数，无论是键还是值都要加双引号，之间用英文逗号隔开,
    # 使用Query String Parameters里的参数获得多页的评论列表
    params ={
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(i + 1),
        'n': '20',
        'w': '周杰伦',
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
    # 向QQ音乐的服务器发送请求，返回有关周杰伦歌曲评论的html代码-.json格式
    # 调用get方法，下载评论列表.
    res_comments = requests.get(url, headers=headers, params=params)
    # 使用json方法，将resopons对象-XHR，转为正常的列表/字典
    # 将参数封装为字典
    res_music = requests.get(url,params=params)
    # 调用get方法，下载这个字典
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    for music in list_music:
        # list_music是一个列表，music是它里面的元素
        # 以name为键，查找歌曲名
        print(music['name'])
        # 查找专辑名
        print('所属专辑：' + music['album']['name'])
        # 查找播放时长
        print('播放时长：' + str(music['interval']) + '秒')
        # 查找播放链接
        print('播放链接：https://y.qq.com/n/yqq/song/' + music['mid'] + '.html\n\n')



