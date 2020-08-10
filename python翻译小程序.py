#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 实现功能：用户输入英文或中文，程序即可打印出来对应的译文。
import requests
import json
from tkinter import Tk, Button, Entry, Label, Text, END


class YouDaoFanyi(object):
    # pass是空语句，填充作用,避免报错
    def __init__(self):
        pass

    def crawl(self, word):
        # python爬虫模拟浏览器访问网站服务器，从浏览中复制Network-Headers-General-Requests Url的网址，进行post提交数据
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.110 Safari/537.36'
        }
        # python爬虫模拟浏览器访问网站服务器，从浏览中复制Network-Headers-Fromdata的内容-即需要post的内容，以字典形式记录在data内
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': 15965249550209,
            'sign': '5bb371e318d90c5a9aafc8d18bf530f1',
            'bv': '7b07590bbf1761eedb1ff6dbfac3c1f0',
            'doctype': 'json',
            'version': 2.1,
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        # 服务器返回内容的是json格式，使用处理字典或列表的方式处理它
        # post返回参数是一个有网站服务器返回得到的json格式的respons对象
        r = requests.post(url, data)
        # 将json格式的字符串转为字典
        answer = json.loads(r.text)
        # 找到translate_0?-XHR,点击Preview，找到翻译内容，对应translateResult-0-0-tag
        result = answer['translateResult'][0][0]['tgt']
        return result


class Application(object):
    # 初始化方法，经过实例化后，不需要调用方法，就能直接使用
    def __init__(self):
        # 初始化方法的属性：window和fanyi
        self.window = Tk()
        self.fanyi = YouDaoFanyi()

        # 进行python GUI设计
        # 设置窗口名称
        self.window.title(u'我的翻译')
        # 设置窗口大小和位置,#310 370为窗口大小，+500 +300定义窗口弹出时的默认展示位置
        self.window.geometry('310x370+500+300')
        self.window.minsize(310, 370)
        self.window.maxsize(310, 370)
        # 创建一个文本框
        # self.entry = Entry(self.window)
        # self.entry.place(x=10, y=10, width=200, height=25)
        # self.entry.bind("<Key-Return>", self.submit1)
        # 背景色：http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        self.result_text1 = Text(self.window, background='azure')
        self.result_text1.place(x=10, y=5, width=285, height=155)
        self.result_text1.bind("<Key-Return>", self.submit1)

        # 创建一个按钮,为按钮添加事件
        self.submit_btn = Button(self.window, text=u'翻译', command=self.submit)
        self.submit_btn.place(x=205, y=165, width=35, height=25)
        self.submit_btn2 = Button(self.window, text=u'清空', command=self.clean)
        self.submit_btn2.place(x=250, y=165, width=35, height=25)

        # 翻译结果标题
        self.title_label = Label(self.window, text=u'翻译结果:')
        self.title_label.place(x=10, y=165)

        # 翻译结果
        self.result_text = Text(self.window, background='light cyan')
        self.result_text.place(x=10, y=190, width=285, height=165)

        # 回车翻译
    def submit1(self,event):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", "")
        # 把这个值传送给服务器进行翻译
        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中
        self.result_text(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    def submit(self):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", "")
        # 把这个值传送给服务器进行翻译
        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中
        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    # 清空文本域中的内容
    def clean(self):
        self.result_text1.delete(0.0, END)
        self.result_text.delete(0.0, END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    # Application类的实例化-app
    app = Application()
    # 调用类的run方法
    app.run()