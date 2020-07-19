# coding=gbk
import requests

res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# 发出请求，并把返回的结果放在变量res中
# 把Reponse对象的内容以二进制数据的形式返回
pic = res.content
# 新建了一个文件ppt.jpg，这里的文件没加路径，它会被保存在程序运行的当前目录下。
# 图片内容需要以二进制wb读写。
photo = open('ppt.jpg', 'wb')
# 获取pic的二进制内容
photo.write(pic)
# 关闭文件
photo.close()
# 通过读写文件把小说保存到本地了
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
res.encoding = 'utf-8'
novel = res.text
fic = open('《三国演义》.txt', 'a+')
fic.write(novel)
fic.close()