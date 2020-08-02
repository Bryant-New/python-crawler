#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
import requests, bs4
import openpyxl

# 创建工作薄
wb = openpyxl.Workbook()
# 获取工作薄的活动表
sheet = wb.active
# 工作表重命名
sheet.title = 'doubanmovie'
# 重新命名表头
sheet['A1'] = '序号'
sheet['B1'] = '电影名'
sheet['C1'] = '评分'
sheet['D1'] = '推荐语'
sheet['E1'] = '链接'

headers={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 寻找豆瓣Top250
# 包含全部目标电影的标签-<div class='article'>
# 包含第一部电影全部信息的标签-<li>..</li>
# 包含第二部电影全部信息的标签-<li>..</li>，每个电影信息由<li>标签控制，article下的25个li标签对应25个电影信息
# for循环了10次，1次爬一页
for x in range(10):
    # start=后面的数字从0每一页加25上去，这时候通过字符串的拼接就可以实现爬取10页url的目的
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    # 提25个li标签,对应25个电影信息，bs.find_all("li")
    # 用len函数print出找到了44个li标签，这说明有19个不要的li标签也提取进来了
    print(len(bs.find_all("li")))
    # ol标签，grid_view属性，可以确定只包含25个有电影信息的li标签
    bs = bs.find('ol', class_="grid_view")
    # for循环进入每个li标签的列表
    for titles in bs.find_all('li'):
        num = titles.find('em', class_="").text
        title = titles.find('span', class_="title").text
        comment = titles.find('span', class_="rating_num").text
        url_movie = titles.find('a')['href']
        if titles.find('span', class_="inq") != None:
            tes = titles.find('span',class_="inq").text
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url_movie)
        else:
            print(num + '.' + title + '——' + comment + '\n' +'\n' + url_movie)
        sheet.append([num, title, comment, tes, url_movie])
# 保存excel
wb.save('豆瓣Top250.xlsx')


