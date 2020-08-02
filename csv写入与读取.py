# coding=gbk
# 引用csv模块，Python自带，不需要自己后面写入,里含open函数，csv模块官方文档链接：
# https://yiyibooks.cn/xx/python_352/library/csv.html#module-csv
import csv

# 创建csv文件，调用open()函数，传入参数：文件名：test.csv,写入模式-
# “w”-以覆盖原内容形式写入新添加的内容、newline=''-结尾不换行-可以避免csv文件出现两倍的行距（就是能避免表格的行与行之间出现空白行）、encoding='utf-8'-编码格式为万国码。
# 打开一个可读写的test.csv文件，并把其内容存到csv_file变量中
csv_file = open('test.csv', 'w', newline='', encoding='utf-8')
# 使用csv.writer()函数创建一个writer对象，进行数据的写入
writer = csv.writer(csv_file)
# 调用writer对象的writerow方法往csv文件中写入新的内容，writerow方法需要放入列表参数
writer.writerow(['电影', '豆瓣评分'])
writer.writerow(['银河护卫队', '8.0'])
writer.writerow(['复仇者联盟', '8.1'])
# 写入文件后，关闭文件
csv_file.close()
# 读取csv文件的数据
import csv
# 用open()打开“test.csv”文件，'r'是read读取模式，newline=''是避免出现两倍行距。encoding='utf-8'能避免编码问题导致的报错或乱码。
csv_file = open('test.csv', 'r', newline='', encoding='utf-8')
# 使用csv.reader函数读取csv_file变量，创建一个reader变量，保存从csv_file变量中读取的内容
reader = csv.reader(csv_file)
# 用for循环遍历reader，打印row，读取出“test.csv”的内容
for row in reader:
    print(row)
csv_file.close()