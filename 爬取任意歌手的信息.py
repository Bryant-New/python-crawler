# 引用requests库和json库
import requests
import json
# 对应歌曲中歌词的具体链接，XHR数据-.json格式数据
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 将python爬虫模拟成浏览器的访问请求,标记请求从什么设备，什么浏览器发出
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
# 刷新歌词网页对应的页码，得到client_search.html网页源代码，内含周董歌曲歌词，复制其Network中对应的Query String Parameters参数
# 获取其对应前五页的歌词
# 输入你喜欢的歌手
singer = input('你喜欢歌手是谁呢？')
for x in range(6):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'txt.yqq.song',
    'searchid':'70717568573156220',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':singer,
    'g_tk':'714057807',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'
    }
    # 将参数封装为字典
    res_music = requests.get(url, headers=headers, params=params)
    # 调用get方法，下载这个列表
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
    # list_music是一个列表，music是它里面的元素
        # 以name为键，查找歌曲名
        print(music['name'])
        # 查找专辑名
        print('所属专辑：'+music['album']['name'])
        # 查找播放时长
        print('播放时长：'+str(music['interval'])+'秒')
        # 查找播放链接
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
