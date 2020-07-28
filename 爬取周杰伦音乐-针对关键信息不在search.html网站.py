import requests
# 引用bs4模块
from bs4 import BeautifulSoup

# 为躲避反爬机制，伪装成浏览器的请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# QQ音乐中对应的周杰伦网址
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=66806524135303302&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
# 向QQ音乐的服务器发送请求，返回有关周杰伦歌曲的html代码
res_music = requests.get(url, headers=headers)
# 使用json方法，将resopons对象-XHR，转为正常的列表/字典
json_music = res_music.json()
print(type(json_music))
# 一层层的取字典，获取歌单列表,data-song-list0-name
list_music = json_music['data']['song']['list']
# list_music是一个列表,music是它里面的元素
for music in list_music:
    # 以name为键，查找歌曲名
    print(music['name'])
# 扩展程序获得歌曲的歌曲名、所属专辑、播放时长，以及播放链接
    # 查找专辑名
    print('所属专辑名：'+music['album']['name'])
    # 查找播放时长
    print('播放时长：'+str(music['interval'])+'秒')
    # 查找播放链接
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')