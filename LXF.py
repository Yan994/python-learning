# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:25:11 2018

@author: Administrator
"""


import numpy

#面向对象编程

class Student(object):
    #类属性
    name='student'
    count=0
    #必须绑定的属性强制填写
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        #每创建一个实例，类属性自动增加
        Student.count+=1
    #为了打印时好看
    def __str__(self):   
        return 'Student object (name:%s,grade:%s)'%(self.name,self.grade)
    __repr__=__str__   #设置相同
    #当调用不存在的属性时，用__getattr__来尝试获得属性
    def __getattr__(self,attr):
        if attr=='age':
            return 22
#类中添加实例
yan=Student('Yan',100)    
yan.name   #'Yan'
yan.age   #22
yan.age=20   #添加新属性
Student.count   #1
#不加.__str__时：
#print(Student('CYY',99))   #<__main__.Student object at 0x00000237DAA964E0>
#加上.__str__后：
print(Student('CYY',99))   #Student object (name:CYY,grade:99)

#实例变量.__name  不会被更改
'''
把Student对象的gender字段对外隐藏起来，
用get_gender()和set_gender()代替，
并检查参数有效性
'''
#定义类：
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self):
        self.__gender=gender
class Goodperson(object):   #好人
    pass
class Badperson(object):   #坏人
    pass
#继承
class MStudent(Student):   #男同学
    pass
    #也可以再定义函数，相同或不同，多态
class FStudent(Student):   #女同学
    pass
#多重继承
class GMStudent(Student,Goodperson):
    pass



#查看数据或函数类型
type(int2)   #functools.partial
#判断是否为函数
import types
def fn():
    pass
type(fn)==types.FunctionType   #True
type(lambda x:x)==types.LambdaType   #True
isinstance([3,2,1,4,5],int)
isinstance([3,2,1,4,5],(list,tuple))   #True
#isinstance也可以判断是否为类
isinstance(yan,Student)   #True

#获取一个对象的所有属性和方法
dir('ABC')   #['__add__','__class__','__contains__',...,'__len__',...]
#关于属性
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()   
#测试是否含属性
hasattr(obj,'x')   #True
#设置属性
setattr(obj,'y',10)
#获取属性值，如果属性不存在，就返回默认值：404
getattr(obj,'y',404)   #10
fn=getattr(obj,'power')
fn()   #81
#同
obj.power()   #81
#一个正确用法例子：从文件流fp中读取图像，首先要判断是否存在read方法
def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None

#__slots__限制实例的属性，即不能对实例自行添加属性，但对继承的自雷不起作用
class Student1(object):
    __slots__=('name','age')
    
# @property 把一个方法变成属性调用
#原来：
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score=value
s=Student()
s.set_score(99)
s.get_score()   #99
#后来：
class Student(object):
    @property   #转换为属性
    def score(self):
        return self._score
    @score.setter   #转换为属性赋值
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')   #自定义错误形式
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score=value
s=Student()
s.score=89
s.score   #89
#可控的属性操作

#练习
class Screen(object):
    @property
    def obj(self):
        pass   #因为是空的，所以s.obj()没有结果
    @obj.setter
    def obj(self,v1,v2):
        self.width=v1
        self.height=v2
    @property   #没有.setter就是只读
    def resolution(self):
        return self.width*self.height
s=Screen()
s.width=1111
s.height=12
s.resolution   #13332

#将类用于for in 循环，需要在类中加入__iter__
#以斐波那契数列为例
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1   #初始化两个计数器
    def __iter__(self):
        return self   #实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a
for i in Fib():
    print(i)
#按list那样照下标取元素，需要__getitem__
class Fib(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
f=Fib()
f[6]   #13
#做切片
class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):   #n是索引
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):   #n是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
Fib()[2:5]   #[2, 3, 5]

#链式调用
class Chain(object):
    def __init__(self,path=''):
        self._path=path
    def __getattr__(self,path):   #没有调用的属性时，返回下面的值，即直接/属性名字/属性名字/
        return Chain('%s/%s'%(self._path,path))
    __call__=__getattr__
    #def __call__(self,path):
    #    return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__

Chain().users('michael').repos   #/users/michael/repos
'''
可以让c=Chain()，c.users就是调用其users属性，但其没有，
所以触动__getattr__，return/属性名字，
再之后c.users()得益于__call__，变成了getattr('michael'),michael直接变成path给return出来
加了__call__的调用，只需要c()，不需要c.call()
'''

#枚举
from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#用来引用一个常量
Month.Jan   #<Month.Jan: 1>
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)
#Jan => Month.Jan , 1
#Feb => Month.Feb , 2

#自定义枚举类型，将属性改造为枚举类型，可以避免使用字符串
from enum import Enum,unique
@unique   #保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6    
print(Weekday.Tue)   #Weekday.Tue
print(Weekday.Tue.value)   #2

#利用type()创建类
def fn(self,name='world'):
    print('Hello,%s!'%name)
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()   #Hello,world!

#错误调试
import logging
try:
    print('try...')
    r=10/0
    print('result:',r)
except ValueError as e:   #如果一个错误为另一个错误的继承，则其会被视为不存在
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except Exception as e:
    logging.exception(e)   #程序打印完错误后仍会继续执行
else:
    print('no error!')
finally:
    print('finally...')
print('END')
#try...
#ZeroDivisionError: division by zero
#zero
#finally...
#END
#常见的错误类型和继承关系
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy

'100+200+300'.split('+')   #['100', '200', '300']
'2018-04-03'.split('-')   #['2018', '04', '03']

#读取UTF-8编码的文本文件
f=open('','r',encoding='',errors='ignore')
f.read()
f.close()
#同
with open('','r') as f :
    print(f.read())
#读取部分
f.read(100)
#读取一行
for line in f.readlines():
    print(line.strip())   #把末尾的‘|n’删掉

#读取二进制文件，比如图片、视频等
f=open('','rb')
#写文本文件或写二进制文件 'w'会覆盖，'a'会添加到末尾
with open('','w') as f :
    f.write('Hello,world!')   #防止没有close而丢失
    



