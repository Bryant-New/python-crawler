#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
import requests, bs4
import csv
from bs4 import BeautifulSoup

# 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''
csv_file = open('articles.csv', 'w', newline='', encoding='utf-8')
#  用csv.writer()函数创建一个writer对象。
writer = csv.writer(csv_file)
# 创建一个列表
list2 = ['标题', '链接', '摘要']
# 调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “标题”和“链接”和"摘要"。
writer.writerow(list2)
# 反爬虫机制，封装header
headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
# 右键检查HTML源代码，Network中的第0个信息有文章标题，-数据存放在网页当中，使用Beautifulsoup来解析数据
# 文章标题对应标签-<a>,属性-target="_blank"和data-za-detail-view-element_name="Title"，搜索target="_blank，发现其结果过多，不能准确定位到文章标题将其舍去
# 超链接标签<a>的target属性指示的是在哪打开跳转的目标网页，"_blank"代表每点击一次超链接打开一个窗口
# 另一个属性data-za-detail-view-element_name="Title"-属性名命名随意，不是html语法中标准的属性名，BeautifulSoup可能不识别，不推荐使用
# 寻找<a>标签的父标签<h2>标签，利用其属性class="ContentItem-title"，精准定位文章标题
# 获取数据-requests库，解析数据BeautifulSoup库，提取数据-用BeautifulSoup库里的find_all方法，翻页则观察第一页到最后一页的网址特征，写循环
# 存储数据用csv或openpyxl模块
# 翻页使用params参数，控制页数

url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# 设置偏移量offset的起始值为第一页的值:10
offset = 10

while True:
    # 封装参数，方便获得多页数据,由Network中的article?的headers里面的query string parameters里的参数
    params = {
        'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
        'offset': '10',
        'limit': '10',
        'sort_by': 'voteups',
    }
    # 获取数据,发送请求，并把响应内容赋值到变量res里面
    res = requests.get(url, headers=headers, params=params)
    # 确认这个response对象状态正确
    print(res.status_code)
    # 获取链接-多次刷新页面得到对应第一页和第二页的参数区别，headers里面的query string parameters里面
    # 发现只有query string parameters中的offset-偏移量不一样，与页码对应，通过循环遍历各页，得到对应页码中的内容
    # 解析数据,解析放在动态网页中的文章，一部分放在网页中，一部分存在xhr中,使用json()方法，将response对象，转为列表/字典

    # 如果响应成功，继续
    if int(res.status_code) == 200:
        # 用json方法解析response对象
        articles = res.json()
        print(articles)
        # 提取数据
        # 层层定位文章标题
        # 提取键为data的值，定位数据
        data = articles['data']
        # 遍历列表，拿到列表里的每一个元素，每一个元素都是字典，通过键把值取出来
        for i in data:
            # 取出文章网址
            # 取出文章摘要
            list1 = [i['title'], i['url'], i['excerpt']]
            writer.writerow(list1)
        # 在while 循环内部,offset的值每次增加20
        offset = offset+20
        if offset>30:
            break
        # 如果offset-偏移量大于30，即爬了两页就停止
        # ——————另一种思路实现————————————————
        # 如果键is_end所对应的值是True，就结束while循环
        # if articles['paging']['is_end'] == True:
            #break
        # 爬取多页
csv_file.close()
print('ok')
