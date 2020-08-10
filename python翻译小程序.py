#  coding: gbk
# Python�������-��ȡ����-��������-��ȡ����-�洢����
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# ʵ�ֹ��ܣ��û�����Ӣ�Ļ����ģ����򼴿ɴ�ӡ������Ӧ�����ġ�
import requests
import json
from tkinter import Tk, Button, Entry, Label, Text, END


class YouDaoFanyi(object):
    # pass�ǿ���䣬�������,���ⱨ��
    def __init__(self):
        pass

    def crawl(self, word):
        # python����ģ�������������վ��������������и���Network-Headers-General-Requests Url����ַ������post�ύ����
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.110 Safari/537.36'
        }
        # python����ģ�������������վ��������������и���Network-Headers-Fromdata������-����Ҫpost�����ݣ����ֵ���ʽ��¼��data��
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
        # �������������ݵ���json��ʽ��ʹ�ô����ֵ���б�ķ�ʽ������
        # post���ز�����һ������վ���������صõ���json��ʽ��respons����
        r = requests.post(url, data)
        # ��json��ʽ���ַ���תΪ�ֵ�
        answer = json.loads(r.text)
        # �ҵ�translate_0?-XHR,���Preview���ҵ��������ݣ���ӦtranslateResult-0-0-tag
        result = answer['translateResult'][0][0]['tgt']
        return result


class Application(object):
    # ��ʼ������������ʵ�����󣬲���Ҫ���÷���������ֱ��ʹ��
    def __init__(self):
        # ��ʼ�����������ԣ�window��fanyi
        self.window = Tk()
        self.fanyi = YouDaoFanyi()

        # ����python GUI���
        # ���ô�������
        self.window.title(u'�ҵķ���')
        # ���ô��ڴ�С��λ��,#310 370Ϊ���ڴ�С��+500 +300���崰�ڵ���ʱ��Ĭ��չʾλ��
        self.window.geometry('310x370+500+300')
        self.window.minsize(310, 370)
        self.window.maxsize(310, 370)
        # ����һ���ı���
        # self.entry = Entry(self.window)
        # self.entry.place(x=10, y=10, width=200, height=25)
        # self.entry.bind("<Key-Return>", self.submit1)
        # ����ɫ��http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        self.result_text1 = Text(self.window, background='azure')
        self.result_text1.place(x=10, y=5, width=285, height=155)
        self.result_text1.bind("<Key-Return>", self.submit1)

        # ����һ����ť,Ϊ��ť����¼�
        self.submit_btn = Button(self.window, text=u'����', command=self.submit)
        self.submit_btn.place(x=205, y=165, width=35, height=25)
        self.submit_btn2 = Button(self.window, text=u'���', command=self.clean)
        self.submit_btn2.place(x=250, y=165, width=35, height=25)

        # ����������
        self.title_label = Label(self.window, text=u'������:')
        self.title_label.place(x=10, y=165)

        # ������
        self.result_text = Text(self.window, background='light cyan')
        self.result_text.place(x=10, y=190, width=285, height=165)

        # �س�����
    def submit1(self,event):
        # ��������ȡ�û������ֵ
        content = self.result_text1.get(0.0, END).strip().replace("\n", "")
        # �����ֵ���͸����������з���
        result = self.fanyi.crawl(content)
        # �������ʾ�ڴ����е��ı�����
        self.result_text(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    def submit(self):
        # ��������ȡ�û������ֵ
        content = self.result_text1.get(0.0, END).strip().replace("\n", "")
        # �����ֵ���͸����������з���
        result = self.fanyi.crawl(content)
        # �������ʾ�ڴ����е��ı�����
        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)

    # ����ı����е�����
    def clean(self):
        self.result_text1.delete(0.0, END)
        self.result_text.delete(0.0, END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    # Application���ʵ����-app
    app = Application()
    # �������run����
    app.run()