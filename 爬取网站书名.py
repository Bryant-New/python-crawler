import requests
from bs4 import BeautifulSoup
res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
html = res_bookstore.text
bs_bookstore = BeautifulSoup(html, 'html.parser')
list_books = bs_bookstore.find_all(class_='product_pod')  # find_all()，是要把每本书都先独立提取出来。接下来，我们再进入每一个<article class="product_pod">下进行数据的提取
for tag_books in list_books:
    tag_name = tag_books.find('h3').find('a')  # 找到a标签需要提取两次
    print(tag_name['title'])