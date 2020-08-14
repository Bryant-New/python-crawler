#  coding: gbk
# Python爬虫过程-获取数据-解析数据-提取数据-存储数据
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium
# 实现功能：我们将完成一个和语义识别相关的爬虫程序，输入任意词汇、句子、文章或段落，会返回联想的词汇。
# 处理语言的网站nlpir：：http://ictclas.nlpir.org/nlpir/
import requests
import json

# “Word2vec”（联想词汇），是一个上传数据，然后服务器解析数据，返回给我们的过程。所以它不会写进网页源代码HTML里，那我们需要查看Network——XHR。
# 打开检查工具，选择Network-XHR，仍然在文本框输入“音乐剧”，然后点击一次“Word2vec”的功能
# 点击Headers确定XHR请求的网址是什么，请求的内容是什么，在Preview（预览）当中，查询返回的联想词汇
# 第0个框，告诉我们请求的网址是：http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do，以及请求的方式POST。
# 第1个框，是我们熟悉的User-Agent。服务器会根据这个信息判断提交请求的是人还是爬虫，所以要封装headers。，将爬虫伪装成浏览器
# 第2个框，就是POST请求所提交的数据。你看到它是一个字典的结构，包含一个键——content，和对应的值——音乐剧。
# 提交这些数据给服务器，服务器会返回给我们一个字典，你可以在Preview中看到
# 封装headers，模拟浏览器向网站服务器提交请求
headers={
    'Origin': 'http://ictclas.nlpir.org',
    'Referer': 'http://ictclas.nlpir.org/nlpir/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/84.0.4147.105 Safari/537.36'
}
# Headers中的requests的url
url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
# 获取需要分析的文本
words = input('请输入你想要查询的词汇:')
# 封装数据内容，我们在Headers面板中的底部看过发送的数据内容是一个字典。
data = {'content': words}
# 发起post请求
res = requests.post(url, headers=headers, data=data)
# res是一个html代码-无法显示文字内容，需要使用.text字符串来显示内容
# res.text将res转为json格式的字符串
data = res.text
# 发送post请求后，我们拿到了返回的数据结果，res.text是一个json格式的字符串。
# 我们只取出主要的联想词汇和其相关系数，即网页中的词汇，和线条上的数值
# 把这个json数据转化成字典，再根据键来取值。要用到json.loads(),使用loads()函数，将json格式的字符串转为字典
data1 = json.loads(data)
# 打印文字
print('和“'+words+'”相关的词汇，至少还有：')
# for循环遍历列表
f = 0
# str（数字）-即得数字，str(9)-9
for i in data1['w2vlist']:
    f = f+1
    #  指定分隔符是逗号，每碰到一个逗号，就切一下。
    word = i.split(',')
    print('('+str(f)+')'+word[0]+'，其相关度为'+word[1])  # 打印数据
    print(str(f))