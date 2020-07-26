import requests
from bs4 import BeautifulSoup

# 获取数据
res_foods = requests.get('http://www.xiachufang.com/explore/')
print(res_foods.status_code)
# 解析数据
bs_foods = BeautifulSoup(res_foods.text, 'html.parser')
# 打印解析结果
print(bs_foods)
# 提取最小父级标签-包括所有的菜名、URL、和食材-循环的主体
list_food = bs_foods.find_all('div', class_='info pure-u')
print(list_food)
# 写循环存所有列表
# 创建一个空列表用于存储信息
list_all = []
for food in list_food:
    # 查找结果中对应的菜名、URL、食材
    # 提取第0个父级标签中的<a>标签-得到菜名对应的html代码，使用text方法改成可视化信息
    tag_a = food.find('a')
    # 菜名，使用[17:-13]切掉了多余的信息
    name = tag_a.text[17:-13]
    # 获取URL
    URL = 'http://www.xiachufang.com' + tag_a['href']
    # 提取第0个父级标签中的<p>标签,得到对应的html代码，需要使用text才能转换成人类语言
    tag_p = food.find('p', class_='ing ellipsis')
    #  食材，使用[1:-1]切掉了多余的信息
    ingredients = tag_p.text[1:-1]
    # 将菜名、URL、食材，封装为列表，添加进list_all
    list_all.append([name, URL, ingredients])
print(list_all)
# text获取到的是该标签内的纯文本信息,text也能获得它子标签的文本信息，但提取标签的属性值只能是本标签的，无法获得子标签的属性值
# 提取奇怪的东西
# 数量太多而无规律，我们会换个标签提取；数量不多而有规律，我们会对提取的结果进行筛选——只要列表中的若干个元素就好。