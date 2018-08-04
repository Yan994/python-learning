# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:57:12 2018

@author: Administrator
"""

#定义函数

def func():
    pass   #暂时闲置
    
#定义函数计算一元二次方程的根
    
import math
def quadratic(a, b, c):
    if a<=0:
        print('这不是一元二次方程！')
    else:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return(x1,x2)
        
        
        
#定义函数中包含位置参数、默认参数
        
def power(x,n=2):
    s=1
    while n>0:
        s=s*x
        n-=1
    return s        
power(5)   #25
power(5,3)   #125

#坑
def add_end(L=[]):
    L.append('END')
    return L
add_end()   #['END']
add_end()   #['END', 'END']

#更改为
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
add_end()   #['END']
add_end()   #['END']



#定义可变参数

#计算a^2+b^2+c^2+...

def calc(numbers):
    sum=0
    for num in numbers:
        sum+=num**2
    return sum
calc([1,2,3])

#同

def calc2(*numbers):
    sum=0
    for num in numbers:
        sum+=num**2
    return sum
calc2(1,2,3)

#同  *将list或tuple的元素变成可变参数传进去

nums=[1,2,3]
calc2(*nums)



#关键字参数   其他暂未定义名称的变量

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
person('Yan',20,city='xm',job='student')   #name: Yan age: 20 other: {'city': 'xm', 'job': 'student'}    
#同
extra={'city': 'xm', 'job': 'student'}
person('Yan',20,**extra)

#命名关键字参数，即限定可加入的关键字参数，而且必须输入参数名，可以为默认参数

def person2(name,age,*,city='xm',job):
    print(name,age,city,job)
person2('Yan',20,job='student')   #Yan 20 xm student

#含可变参数时，不必再加*

def person3(name,age,*num,city,job):
    print(name,age,num,city,job)
person3('Yan',20,city='xm',job='student')    

#参数顺序

def ff(a,b,c=0,*num,**kw):
    print('a=',a,'b=',b,'c=',c,'num=',num,'kw=',kw)
ff(1,2,c=3)   #a= 1 b= 2 c= 3 num= () kw= {}
ff(1,2,3,'a','b',d=4)   #a= 1 b= 2 c= 3 num= ('a', 'b') kw= {'d': 4}

#同

num=(1,2,3,'a','b')
kw={'d':4}
ff(*num,**kw)   #a= 1 b= 2 c= 3 num= ('a', 'b') kw= {'d': 4}

#练习

def product(*numbers):
    pro=1
    if numbers==():
        raise TypeError
    else:
        for num in numbers:
            pro*=num
        return pro
product(2,5)



#递归函数

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
fact(5)

#练习

#汉诺塔移动
#move(n,a,b,c)接收参数n表示a的盘子数量，要把所有盘子从a借助b移动到c

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)#a柱最上方的n-1个盘子落在b柱
        move(1,a,b,c)#a柱最下面的盘子落在c柱
        move(n-1,b,a,c)#b柱上的n-1个盘子落在c柱
move(3,'A','B','C')