#  coding: gbk
# QQ音乐评论-动态网页-爬取的数据不在HTML源代码中，而是在json中，需要找到其对应得XHR获得其requests url网址和参数进行爬虫
# 爬取周董歌曲《甜甜的》
# 网页源代码中没有我们想要的评论，而是存在了Json中，需要通过查看XHR，找到每一页评论的Json数据真实URL，才能获取到数据。
# 用selenium，就不需要花费精力去查找和破解URL了，因为，通过selenium打开浏览器的操作，数据就被加载到elements中了
# 获取更多的评论的方法，也变得非常简单，直接使用selenium控制浏览器点击【点击加载更多】的按钮，评论数据自然就都加载到elements中了
# 解析与提取数据：第一种解决思路是使用selenium提取数据的方法。第二种解决思路是，先获取到完整网页源代码，然后用BeautifulSoup抓取
# 评论所在的元素中，class属性就有好多个，而使用selenium时，只能用其中一个属性来提取数据
# 通过分析网页结构，我们选择用class_name与tag_name来提取数据-一次性获得15个评论数据
# comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
# print(len(comments)) # 打印获取到的评论个数
# for comment in comments: # 循环
#     sweet = comment.find_element_by_tag_name('p') # 找到评论
#     print ('评论：%s\n ---\n'%sweet.text) # 打印评论
# driver.close() # 关闭浏览器
# 下一步，我们要获取更多评论。点击网页中的【点击加载更多】，就会加载出新的15个评论的数据。首先找到【点击加载更多】在网页源代码中的位置，
# 点击它，等待源代码加载完成之后就可以把全部30个评论提取出来了。