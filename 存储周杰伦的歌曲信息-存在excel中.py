#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
import requests
import openpyxl

# Excel文件写入：1.创建工作薄2.获取工作表3.操作单元格4.保存工作薄
# 创建工作薄
wb = openpyxl.Workbook()
# 获取工作薄的活动表
sheet = wb.active
# 工作表重命名
sheet.title = 'song'
# 往excel表中添加表头：歌曲名、所属专辑、播放时长和播放链接
# 分别在A1、B1、C1、D1单元格中写入“歌曲名”、“所属专辑”、“播放时长”和“播放链接”。
sheet['A1'] = '歌曲名'  # 加表头，给A1单元格赋值
sheet['B1'] = '所属专辑'  # 加表头，给B1单元格赋值
sheet['C1'] = '播放时长'  # 加表头，给C1单元格赋值
sheet['D1'] = '播放链接'  # 加表头，给D1单元格赋值

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# 将python爬虫模拟成浏览器的访问请求,标记请求从什么设备，什么浏览器发出
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}
for x in range(5):
    # 将参数封装为字典
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
    # 调用get方法，下载这个列表--获取数据
    res_music = requests.get(url, params=params, headers=headers)
    # 使用json()方法，将response对象，转为列表/字典-解析数据
    json_music = res_music.json()
    # 一层一层地取字典，获取歌单列表-提取数据
    list_music = json_music['data']['song']['list']

    # list_music是一个列表，music是它里面的元素
    for music in list_music:
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        name = music['name']
        # 查找专辑名，把专辑名赋给album
        album = music['album']['name']
        # 查找播放时长，把时长赋值给time
        time = music['interval']
        # 查找播放链接，把链接赋值给link
        link = 'https://y.qq.com/n/yqq/song/' + str(music['mid']) + '.html\n\n'
        # 把name、album、time和link写成列表，用append函数多行写入Excel
        sheet.append([name, album, time, link])
        print('歌曲名：' + name + '\n' + '所属专辑:' + album + '\n' + '播放时长:' + str(time) + '\n' + '播放链接:' + link)

# 最后保存并命名这个Excel文件
wb.save('Jay.xlsx')


