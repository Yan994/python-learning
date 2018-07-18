# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 18:58:27 2017

@author: Administrator
"""

'''
conda list 查看包
包 scipy 做科学计算，解方程，做模拟
包 scikit-learn 继续学习
包 seaborn 画图，可视化
包 requests 做HTMP 大批量访问网页  爬数据
包 numpy 关于matlab
包 networkx 社交网络 数学中图论 找最短路径
conda install  安装新的东西
pip install *** requests
python  检查是否正确安装
quit()  删除包
'''

print('Hello World')
print('100+200=',100+200)
#out:100+200= 300

#列表（容器，数据长度可变化）

a=[]     #创建列表
b=[2,6,3,7,1]

a.append(1)     #在a中添加元素,每次只能加一个
a.append(2)
a.append(3)

print(a)     #输出a
print(b[1:3])     #输出b中第2至第3个数值
print(3 in b)     #验证b中是否有数值3，结果是TRUE
print(sorted(b))     #输出排序后的数值

del b[1]     #删除b中第2个的元素

c=["cheng","yan","yan"]     #输入字符型数据
#前面加上print才会在运行多行代码中显示出来
print(len(b))     #长度
sum(b)     #求和
min(b)
max(b)

def average(seq):
    return float(sum(seq))/len(seq)
average(b)     #不能直接求均值，需要先定义

3/5     #结果是0.6.(取整是python2)
float(3)/float(5)     #结果是0.6
5%3    #取余

for i in b:
    print(i)     #列表的遍历，列出b中的每个元素
for i in range(0,len(b)):
    print(b[i])     #同上

b[0]     #列表的索引，找出b中的第几个元素，注：0代表第一个元素

d=a+b     #列表的合并,不是求和，是组成一个更长的向量

#元组  不能更改  不能用append添加

e=(1,2,3)     #元组的创建
f=(4,5,6,7)

g=e+f     #元组的合并，依然是合并成一个更长的元组

#字符串  不能更改  可以被分解

h="hello world"     #字符串的创建

type(h)     #查看数值类型

h[4]     #分解，输出第5个字母，依然0是第一个，空格也算一个

i="600519.SH"
i.replace(".SH","")     #替换，将前面的（原来有的）替换成后面的
print(i)     #结果是替换之前的
j=i.replace(".SH","")     #把替换后的保存下来

#字典对象


k={'a':1,'b':2,'c':3,'d':4,'e':5}     #创建字典对象，之后访问冒号前，得到冒号后

print(k['a'])
print(k.keys())          #输出的是dict_keys(['a', 'b', 'c', 'd', 'e'])
print(k[list(k.keys())[0]])     #结果同上

for i in k.keys():
    print(k[i])     #结果同下，但输出是几个单个数值

print(k.values())     #输出冒号后的所有值，组成了一个向量

print(list(k.keys()))     #输出冒号前的所有键
if 'c' in k:
    print('True')     #是否k中含有键c

del k['a']

zip(('x','y','z'),(1,2,3))     #将前后分别组合

import pandas as pd
print(pd.Series(k))     #以序列形式表示
print(pd.DataFrame({'a':k,'d':k}))    #又把k序列赋予键a和键d

#定义一个字符串
str1="3w.gorly.test.com.cn"
#指定分隔符为'.'，并且指定切割次数为1次
print(str1.split('.',1))
#['3w', 'gorly.test.com.cn']
print(str1.split('.')[0])
#3w

#统计字符串中出现的单词个数
str2="To be or not to be, this is a question"
print(len(str2.split(' ')))
#10

#将从html代码中提取网站地址
s='<a href="www.test.com">test</a>'
print(s.split('"')[1])
#www.test.com
print(s.split('"')[1].split('.'))
#['www', 'test', 'com']

#去掉字符串中的换行符\n
str3='''hello
world
!'''
str3.split('\n')
#['hello', 'world', '!']

#分割文件和其路径
import os
print(os.path.split("d:\test\a.txt"))
#('d:', '\test\x07.txt')
print(os.path.split("d:/test/a.txt"))
#('d:/test', 'a.txt')


#普通字符串的连接
'-'.join("abcdef")
#'a-b-c-d-e-f'
''.join(['ab','cd','ef'])
#'abcdef'