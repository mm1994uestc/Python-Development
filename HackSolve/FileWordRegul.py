import re
import math
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

'''
link = 'http://news.sina.com.cn/'
res = requests.get(link)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
alink = soup.select('a')
DATA = set()
Cookies = ['读书', '教育', '天气', '军事']
for link in alink:
    if link.text in Cookies:
        Temp = 'The title of link '+link.text+' is :'+link['href']
        DATA.add(Temp)
for Info in DATA:
    print(Info)
Check = input('Please input the content you want to see:')
Str = ''
for W in list(DATA):
    if W.find(Check) != -1:
        Str = Str + W + '\n'
File = open('C:\\Users\\Administrator\Desktop\Python爬虫准备\demo\Info.txt', 'w')
File.writelines(Str)
File.close()
'''

HTML = 'http://book.weibo.com/newcms/tp_p4c51t160.html'
res = requests.get(HTML)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select('p')
print(len(title))

