import requests
from bs4 import BeautifulSoup
# 获取数据
res_food = requests.get('http://www.xiachufang.com/explore/')
print(res_food.status_code)
# 解析数据
bs_food = BeautifulSoup(res_food.text, 'html.parser')
# 查找包含菜名和URL的<p>标签-使用find_all方法得到对应tag对象，是html代码，要经过text翻译
tag_name = bs_food.find_all('p', class_='name')
# 查找包含食材的<p>标签
tag_ingredients = bs_food.find_all('p', class_='int ellipsis')
# 创建一个空列表,用于存储信息
list_all = []
# 启动循环，次数名等于菜名的数量
for x in range(len(tag_name)):
    # 提取信息，封装为列表
    list_food = [tag_name[x].text[18:-14], tag_name[x].find('a')['href'], tag_ingredients[x].text[1:-1]]
    list_all.append[list_food]
print(list_all)
