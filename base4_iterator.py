# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:36:50 2018

@author: Administrator
"""

#练习，切片加递归

def trim(s):
    if s=='':
        return ''
    elif s[:1]==' ':
        return trim(s[1:])  
    elif s[-1:]==' ':      #从最后一个开始往后
        return trim(s[:-1])#从第一个开始到最后一个
    else:
        return s  
trim('hello  ')
trim('  hello')
trim('  hello  ')



#判断一个对象是否为可迭代对象

from collections import Iterable
isinstance(123,Iterable)   #False

#enumerate

for i,value in enumerate(['A','B','C']):
    print(i,value)   #0 A   1 B   2 C

#练习
#使用迭代查找一个list中最小和最大值，并返回一个tuple

def findMinAndMax(L):
    if L==[]:
        return (None,None)
    min=L[0]
    max=L[0]
    for l in L:
        if min>l:
            min=l
        if max<l:
            max=l
    return(min,max)
    
    

#列表生成式
    
[x*x for x in range(1,11)]   #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[x*x for x in range(1,11) if x<=3]   #[1, 4, 9]
[m+n for m in 'ABC' for n in 'abc']   #['Aa', 'Ab', 'Ac', 'Ba', 'Bb', 'Bc', 'Ca', 'Cb', 'Cc']
#注：+前后必须都为str

dd={'A':'a','B':'b','C':'c'}
[k+'='+v for k,v in dd.items()]   #['A=a', 'B=b', 'C=c']

#把一个list中的字符串变成小写、大写

LL=['Yan','Cheng']
[s.lower() for s in LL]   #['yan', 'cheng']
[s.upper() for s in LL]   #['YAN', 'CHENG']

#isinstance判断是否为str格式

LL.insert(1,123)
[s.lower() if isinstance(s,str)==True else s for s in LL]   #['yan', 123, 'cheng']



#生成器generator,节省空间

g=(x*x for x in range(10))

#取用元素

next(g)   #0
next(g)   #1
for n in g:
    print (n)


#斐波拉契数列（Fibonacci）
#1,1,2,3,5,8,13,21,34,...

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print (b)   #yield b  返回的是generator
        a,b=b,a+b
        n+=1
    return'done'
fib(6)   #1 1 2 3 5 8 'done'

#循环生成generator   

def odd():
    print('step 1')
    yield 1   #遇到即终止，再next从下一步继续
    print('step 2')
    yield 3
    print('step 3')
    yield 5
odd()   #是一个generator
o=odd()
next(o)   #step 1  Out[356]: 1

'''
练习
杨辉三角定义如下：
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''
def triangles(t):
    L=[1]
    n=1
    while n<(t+2):
        yield(L)
        L=[(L+[0])[i]+([0]+L)[i] for i in range(len(L)+1)]
        n+=1
for x in triangles(9):
    print(x)

L=[1]
L+[1]   #[1, 1]

#使用isinstance(,)判断是否为可迭代对象Iterable、迭代器Iterator
#生成器都是Iterator对象
#使用iter()把list、dict、str等Iterable变成Iterator

from collections import Iterator
isinstance(iter([]), Iterator)   #True