import re
import math
import json
import urllib
import requests
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime
'''
# This is a simple test for using those tools:Beautifulsoup+requests
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'html.parser')

alink = soup.select('a')
print('The type alink is:', alink)
for link in alink:
    print('The ', link['id'], ' is :', link['href'])

Title = soup.select('title')
print(Title)
'''


link = 'http://news.sina.com.cn/'
res = requests.get(link)
res.encoding = 'utf-8' #设置文本的编码格式是utf-8的文件格式
soup = BeautifulSoup(res.text, 'html.parser') #通过res中的成员变量.text来得到HTML的文本res.text
alink = soup.select('a') #选择class模块中的a来作为提取的目标的判定条件：<a href="http://mil.news.sina.com.cn/"><span class="titName ptn_05">军事</span></a>
DATA = set() #创建一个set集合
Cookies = ['军事', '教育', '科技', '文化'] #创建一个目标提取项目
for link in alink:
    if link.text in Cookies: #alink中包含了所有的以a开头的class文本，link.text提取了其中一个link的文本内容
        Temp = 'The title of link '+link.text+' is :'+link['href'] #使用link['herf']来取herf对应的字典字符串，也就是对应的链接
        DATA.add(Temp) #在DATA数据中加入满足正则要求的文本文件
for Info in DATA:
    print(Info)
Check = input('Please input the content you want to see:')
Str = ''
for W in list(DATA):
    if W.find(Check) != -1:
        Str = Str + W + '\n'
File = open('C:\\Users\\Administrator\Desktop\Python爬虫准备\demo\Info1.txt', 'w') #将取得的文件写入到文件夹当中
File.writelines(Str)
File.close()

HTML = 'http://book.weibo.com/newcms/tp_p4c51t160.html'
res = requests.get(HTML)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select('.S_title')
print(title[0].text)
content = soup.select('.S_explain')
print(content[0].text)
Count = soup.select('.book_vote')
Bname = soup.select('.book_name')
Aname = soup.select('.book_author')
Blink = soup.select('a')
Info = ''
for i in range(len(Bname)):
    Info = Info + Bname[i].text + '-->' + Aname[i].text + '(' +\
           Count[i].text.replace(' ', '') + ')' + '--link:' +\
           Blink[i*4]['href']+'\n\n'
print(Info)
Data = title[0].text + '\n' + content[0].text + '\n' + Info
F = open('C:\\Users\\Administrator\Desktop\Python爬虫准备\demo\Info2.txt', 'w')
F.writelines(Data)
F.close()

Init_link = 'https://www.douyu.com/directory/all'
Data = requests.get(Init_link)
Data.encoding = 'utf-8'
soup = BeautifulSoup(Data.text, 'html.parser')
Res = soup.select('.mes')
Count = soup.select('p')
for i in Res:
    if i.text.find('英雄联盟') != -1:
        Str = i.text.replace(' ', '').replace('\n', '')
        print(Str)
        print(Str[len(Str)-3:len(Str)])
print(len(Res))

