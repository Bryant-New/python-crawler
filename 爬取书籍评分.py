import requests
from bs4 import BeautifulSoup

res_bookstore = requests.get('http://books.toscrape.com/catalogue/category/books/travel_2/index.html')
bs_bookstore = BeautifulSoup(res_bookstore.text,'html.parser')
list_books = bs_bookstore.find_all(class_='product_pod')
for tag_books in list_books:
    list_star = tag_books.find('p',class_="star-rating")
    # 这个p标签的class属性有两种："star-rating"，以及具体的几星比如"Two"。我们选择所有书都有的class属性："star-rating"

    print('star-rating:', list_star['class'][1])
