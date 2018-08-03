# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:27:29 2018

@author: Administrator
"""

#直接求计算结果

100+200  #300

#关于print()

print (100+200)   #300
print ('100+200=',100+200)   #100+200= 300
print ('Hello World!')   #Hello World!

#关于input()

name=input()   #
print (name)

#把str转换为数值

int('123')   #123  整数
int(123.123)   #123
float('123.123')   #123.123   原数

name=input('please enter your name:')
print ('Hello',name,'!')   #逗号显示为一个空格

#转义字符\

print('I\'m "OK"!')
print('\'n\'')   #'n'
print('\\')   #\

#\n 表示换行，\t 表示制表符，\ 本身也要转义

print('I\'m learning\nPython')
print('\\\t\\')   #\       \
print('\\\n\\')   #\ 转行 \

#r''表示''内部的字符串默认不转义

print(r'I\'m ok!')   #I\'m ok!
print(r'\\\n\\')   #\\\n\\

#'''...'''表示多行内容

print('''x1
x2
x3''')   #这样即可,''不可
print(r'''x1\n
x2''')   #x1\n 转行 x2    即r''''''也不转义

#布尔值，一个布尔值只有True、False两种值

3<4   #True

#可以用and,or,not运算

3<4 and 3<2   #False
3<4 or 3<2   #True
not 3<4   #False

#空值
None

#变量
a = 1
b = 'b'

#除法
10/3   #3.3333333333333335
9/3   #3.0
10//3   #3
10%3   #1   余数


#练习:
#请打印出以下变量的值：

# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('',n,'\n',f,'\n',s1,'\n',s2,'\n',s3,'\n',s4)
print(n,f,s1,s2,s3,s4,sep='\n')  

  
    
'''
关于编码
最早英文数字等，用ASCII编码；
中文超出ASCII编码范围，出现Unicode编码；
所需存储空间太大，出现UTF-8编码，有一部分同ASCII编码，又利于存储
'''

#ord()获取字符的整数表示，chr()把编码转换为对应的字符 
   
ord('c')   #99
ord('C')   #67
ord('成')   #25104
chr(66)   #'B'
chr(23721)   #'岩'

#如果知道字符的整数编码，还可以用十六进制这么写str：
'\u4e2d\u6587'   #'中文'

#Python的字符串类型是str,如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
'成岩岩'.encode('utf-8')   #b'\xe6\x88\x90\xe5\xb2\xa9\xe5\xb2\xa9'
'CYY'.encode('ascii')   #b'CYY'

#在bytes中，无法显示为ASCII字符的字节，用\x##显示       

b'\xe6\x88\x90\xe5\xb2\xa9\xe5\xb2\xa9'.decode('utf-8')   #'成岩岩'
b'\xe6\x88\x90\xff'.decode('utf-8',errors='ignore')   #'成'

#计算str包含多少个字符

len('成岩岩')   #3
len('CYY')   #3

#如果换成bytes，len()函数就计算字节数

len(b'\xe6\x88\x90')   #3
len('成岩岩'.encode('utf-8'))   #9

#占位符%
'''
#%是用来格式化字符串的。
#在字符串内部，%s表示用字符串替换
#%d表示用整数替换
#%f表示用浮点数替换
#%x表示用十六进制整数替换
#可有多个%?占位符
'''

name=input('please enter your name:')
'Hello,%s'% name   #'Hello,成岩岩'
'Hi, %s, you have $%d.' % (name,10000)   #'Hi, 成岩岩, you have $10000.'

#可以控制被替换的位数

print('%d-%02d' % (3,1))      #3-01
print('%2d-%02d' % (3,1))     # 3-01
print('%002d-%002d' % (3,1))  #03-01
print('%003d-%003d' % (3,1))  #003-001
print('%.2f' % 3.14159)   #3.14

#%的转义是%%

print('the percent is %s%%' % 5)    #the percent is 5%
'Hello, {0}, you have ${1:.1f}'.format('Yan',19.23)   #'Hello, Yan, you have $19.2'


#练习

s1=int(input('去年分数：'))
s2=int(input('今年分数：'))
r=(s2-s1)/s1*100
print('%s的成绩提高了%.1f%%.' % ('小明',r))