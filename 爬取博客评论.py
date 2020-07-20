import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
#
for x in range(1, 545):
    destnation_url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/comment-page-'+str(x)+'/#comments'
    # 把网址复制给变量destnation_url
    destnation = requests.get (destnation_url)  # 返回一个response对象，赋值给destnation
    soup = BeautifulSoup(destnation.text, 'html.parser') # 把网页解析为BeautifulSoup对象
    comments = soup.find_all('div', class_='comment-content') #通过匹配属性提取出我们想要的元素

    for comment in comments:  # 遍历列表，取出列表中的每一个值
        print(comment.text)  # 打印评论的文本