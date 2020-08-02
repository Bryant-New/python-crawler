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
for x in range(5):
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.lyric_next',
        'searchid': '94267071827046963',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'sem': '1',
        't': '7',
        'p': str(x + 1),
        'n': '10',
        'w': '周杰伦',
        'g_tk': '1714057807',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
# 使用requests库函数下载该网页
    res_lyric = requests.get(url, headers=headers, params=params)
# 使用json来解析res_lyric.text
    jsonres = json.loads(res_lyric.text)
# 一层层的取字典，获取歌词的列表
    list_lyric = jsonres['data']['lyric']['list']
# 遍历歌词列表
    for lyric in list_lyric:
        # 以CONTENT为键查找歌词
        print(lyric['content'])