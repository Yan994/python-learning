# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 18:25:11 2018

@author: Administrator
"""

#面向对象编程
#数据封装、继承、多态

class Student(object):
    #类属性，类的实例可以访问但不能修改
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
    #给类增加新方法
    def get_grade(self):
        if self.grade>=90:
            return 'A'
        else:
            return 'B'
        
#类中添加实例

yan=Student('Yan',100)    
print(yan.name)   #Yan
print(yan.age)   #22
print(yan.get_grade())   #A
yan.age=20   #添加新属性
print(Student.count)   #1

#不加.__str__时：
#print(Student('CYY',99))   #<__main__.Student object at 0x00000237DAA964E0>
#加上.__str__后：
print(Student('CYY',99))   #Student object (name:CYY,grade:99)

#实例变量.__name  不会被更改

'''
把Student对象的gender字段对外隐藏起来，
用get_gender()和set_gender()代替，
并检查参数有效性（在set_gender()中设置错误检查）
'''

#定义类：

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
class Goodperson(object):   #好人
    pass
class Badperson(object):   #坏人
    pass

yan=Student('Yan','女')
print(yan)
print(yan.get_gender()) #女
yan.set_gender('男')
print(yan.get_gender()) #男

#继承，自动包含父类的所有方法

class Student(object):   #父类
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def get_gender(self):
        return self.gender

class MStudent(Student):   #男同学  子类
    pass
yan_M=MStudent('Yan_M','男')
print(yan_M.get_gender())   #男

#也可以再定义函数，相同或不同，多态

class MStudent(Student):   #男同学  子类
    def get_gender(self):
        if self.gender == '男':
            return 'man'
        else:
            return 'woman'
yan_M=MStudent('Yan_M','男')
print(yan_M.get_gender())   #man

#多重继承，继承多个父类
class GMStudent(Student,Goodperson):
    pass



#查看数据或函数类型
#type()   

#判断是否为函数

import types

def fn():
    pass

type(fn)==types.FunctionType   #True
type(lambda x:x)==types.LambdaType   #True

#判断类型

isinstance([3,2,1,4,5],int)

#判断是否为类型中的一种

isinstance([3,2,1,4,5],(list,tuple))   #True

#isinstance也可以判断是否为某类

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

#测试是否含某属性

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

#__slots__限制实例的属性，即不能对实例自行添加属性，但对继承的子类不起作用

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