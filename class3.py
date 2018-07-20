# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:27:08 2017

@author: Administrator
"""
'''
爬数据
关系型数据库mySQL,SQLsewer，非关系型数据库key_value

建立数据库连接、建立搜索引擎、输入执行语句、调取数据

import pandas as pd
import pymysql
import pymasql
from sql

set 建立连接  type IP 用户名 账号密码 数据名称

传变量名
判断是什么数据库

搜索语句  select *所有 A B
search 

where 指定名称 做条件筛选

boding bound
算upper bound,lower bound


从网络爬数据
http协议 
URL  网址
传输方式  get  post
状态码 404表示出错
URL结构  爬虫需要拼接构造URL   ?后面是查询参数 sort排序

请求报文   、响应报文
构造请求
headers  ua限制次数，换ua，换IP

HTML结构

导入包
r.content 爬的内容
r.text 文字
r.encoding

地点位置解析
URL
地点位置转URL编码

headers  复制的

Tushare 免费开源财经数据库
'''
#一个关于cars的例子
import requests     #请求报文
from bs4 import BeautifulSoup    #from 主体名称是子数据库名称
import re
import pandas as pd

html=requests.get(    #网址
            'http://mt.sohu.com/20161016/n470376857.shtml').content
            #网站所有内容信息
print html
'''
</div>
<article class="article">
      <p data-role="original-title" style="display:none">原标题：2016全球最有价值的100大汽车品牌 14个中国品牌上榜</p>
            <p>英国品牌评估机构Brand Finance发布“2016汽车品牌百强和轮胎品牌十强榜”(Brand Finance Auto 100 &amp; Tyres 10 2016)。在全球价值最高的前十大汽车品牌中，日本丰田以430.64亿美元的品牌价值名列榜首，德国宝马和梅赛德斯奔驰分列第二和第三位。丰田的品牌价值比上年度增加了23%，而由于排放门的影响，大众的品牌价值比上年度下降了39%。</p> 
<p>100强汽车品牌中既包括了轿车品牌，也有卡车、摩托车和汽车零部件品牌。共有14个中国汽车品牌进入百强榜，排名最高的长城汽车列第30位。</p> 
<p><strong>排名 品牌 归属地 品牌价值/增长率 所属集团</strong></p> 
<p>1.丰田(Toyota) 日本 430.64亿美元/23% 丰田集团</p> 
<p><img src="http://img.mp.itc.cn/upload/20161016/f7a3d3a59a174ec6a48a5437467da5c9.jpeg" /></p> 
<p>2.宝马(BMW) 德国 349.68亿美元/6% 宝马集团</p> 
<p><img src="http://img.mp.itc.cn/upload/20161016/cc66213cfab44fbfb5b4bfca49a30aac.gif" /></p> 
<p>3.梅赛德斯奔驰(Mercedes-Benz) 德国 320.49亿美元/17% 戴姆勒集团</p> 
<p><img src="http://img.mp.itc.cn/upload/20161016/11030516979c4adf9710287de4c7c1c5.jpeg" /></p> 
<p>4.福特(Ford) 美国 197.71亿美元/-3% 福特汽车</p> 
'''

container=BeautifulSoup(html,"lxml").body.find(
            'div',attrs={'class':'text'}).find_all('p')
                                         #p是前后包含所需内容的
table = []     #range的是p的位置，从第4个p包含的内容开始
for i in range(3,len(container)):
      try:
            content=container[i].get_text() #获取内容，如下
            #1.丰田(Toyota) 日本 430.64亿美元/23% 丰田集团
            #变成正则表达式 数字.非数字()非数字
            rank=re.findall('\d*\.',content)[0].replace('.','')
            name=re.findall('\.\D*\(',content)[0].replace('.','').replace('(','')
            country=re.findall('\)\D*',content)[0].replace('.','').replace(')','')
            table.append([name,rank,country])
      except:
            pass
print pd.DataFrame(table,columns=['name','rank','country'])
'''
       name rank     country
0        丰田    1         日本 
1        宝马    2         德国 
2    梅赛德斯奔驰    3         德国 
3        福特    4         美国 
4        本田    5         日本 
5        大众    6         德国 
'''


#another example
url = 'http://www.qianlima.com/zb/area_305/'  
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'  
headers = { 'User-Agent' : user_agent}  
r = requests.get(url,headers=headers)#连接  
content = r.text#获取内容，自动转码unicode  
soup = BeautifulSoup(content,"lxml")  
tags1 = soup.select('div .shixian_zhaobiao')  
tag1 = tags1[0]  
tag2 = tag1.find(name = 'dl')
tags2 = tag2.find_all(name = 'a')  
tags3 = tag2.find_all(name = 'dd')  
for tag in tags2:  
    print tag.get('href')  
    print tag.string  
    print tag.next_element.next_element.string  