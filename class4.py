# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:23:52 2017

@author: Administrator
"""
'''
内容概况：
1、爬虫原理介绍；
2、反爬机制与爬虫程序实现；
3、常用数据的导入与获取。

文本解析
   
pip install bs4 安装包
'''
from bs4 import BeautifulSoup
'''
soup=BeautifulSoup(      object      ,    "html.parser")
                   #request.get().content   或者"lxml"(最好)、"html5lib"
bs4  BeautifulSoup 建立树状结构 适合网站信息比较规律、容易定位的
html
   head
       div
          span
              a
   body
       div
       di
'''

'''
re   regular expression正则表达式 留规律，删不规律
     \d*\-\d*\-\d*      *表示一次或多次   \. 任意字符   \D 非数字
     2017-09-15
'''

'''
搜索标签 search方法
TAG标签 html.body.div.div.div 一层层写
find   找到符合特征的，返回第一个结果，适合独一无二的结果
find_all 返回列表结构 
find(name,attrs)
body之下div(只有1个)之下p(最小一级)
.body.find('div',attrs={'class':'text'}).find_all('p')
'''

#pandas 面板数据分析  序列 DataFrame 
#IO tools
import pandas
#pandas.read_csv(filepath,header,names,skiprows,encoding)
                         #开头行       #剔数据
#pandas.read_excel(filepath,sheetname,header,names,skiprows,encoding)







