import requests
from bs4 import BeautifulSoup
res_bookstore = requests.get('http://books.toscrape.com/')
html = res_bookstore.text
bs_bookstore = BeautifulSoup(html, 'html.parser')
list_kind = bs_bookstore.find('ul', class_='nav').find_all('li')
for tag_kind in list_kind:
    tag_name = tag_kind.find('a')  # tag_name.text是提取出<a>标签的文本部分，.strip() 是将文本部分的特殊字符切除，
    print(tag_name.text.strip())  # 去除特殊字符串，比如空格，\n，\t等等