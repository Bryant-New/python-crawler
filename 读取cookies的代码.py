import json
import requests
# 以reader读取模式，打开名为cookies.txt的文件。
cookie_txt = open('cookies.txt', 'r')
# 调用json模块的loads函数，把字符串转成字典
cookies_dict = json.loads(cookie_txt.read())
# 把转成字典的cookies再转成cookies本来的格式。
cookies = requests.utils.cookiejar_from_dict(cookies_dict)
# 获取cookies：就是调用requests对象（session）的cookies属性。
session.cookies = cookies
