# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 15:56:36 2018

@author: Administrator
"""

#高阶函数

def add(x,y,f):
    print(f(x)+f(y))
add(-2,3,abs)   #5

#关于map

def f(x):
    return x*x
r=map(f,[1,2,3,4,5])
list(r)
list(map(str,[1,2,3]))   #['1', '2', '3']

#关于reduce,reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)

from functools import reduce

def add(x,y):
    return x+y
reduce(add,[1,3,5,7])   #16

def fn(x,y):
    return x*10+y
reduce(fn,[1,3,5,7])   #1357

#变首字母为大写

def normalize(name):
    return name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize,L1))

#变字符串为数字(以键取值)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#filter过滤序列(留下满足条件的，所需函数返回的结果是逻辑)
    
def is_odd(n):
    return n%2==1
list(filter(is_odd,[1,2,3,4,5]))   #[1, 3, 5]

#删除序列中的空字符串

def not_empty(s):
    return s and s.strip()
list(filter(not_empty,['a','b',None,'c','']))   #['a', 'b', 'c']

'a' and 'b'   #'b'
'b' and 'a'   #'a'
'a' and None   #
None and 'a'   #
'b' or 'a'   #'b'
None or 'a'   #'a'
1<2 and 2<3   #True

#生成素数

def _odd_iter():
    n=3
    while True:
        n+=2
        yield n
def _not_divisible(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd_iter()   #初始序列
    while True:
        n=next(it)   #返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)   #构造新序列
for n in primes():
    if n<=1000:
        print(n)
    else:
        break
#将数字倒过来的字符串
str(123)[::-1]   #'321'
#判断数字是否为回数，即121,12321
def is_palindrome(n):
    return str(n)==str(n)[::-1]
list(filter(is_palindrome,range(1000)))

#sorted 对list排序
sorted([3,6,1,7,-5])   #[-5, 1, 3, 6, 7]
sorted([3,6,1,7,-5],key=abs)   #[1, 3, -5, 6, 7]
sorted(['bob', 'about', 'Zoo', 'Credit'])   #['Credit', 'Zoo', 'about', 'bob']
sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)   #['about', 'bob', 'Credit', 'Zoo']
#对tuple排名
L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按姓名
def by_name(t):
    return t[0].lower()
sorted(L,key=by_name)
#按成绩从高到低
def by_grade(t):
    return -t[-1]   #取个相反数
sorted(L,key=by_grade)

#返回函数
def createCounter(): #外部函数
    n=0
    def counter():   #内部函数
        nonlocal n   #再次调用内部函数时会改变外部函数参数
        n+=1
        return n
    return counter   #返回的是个函数
counterA=createCounter()
print(counterA(),counterA(),counterA())   #1 2 3
counterB=createCounter()
print(counterB())   #1

# f._name_  取函数的名字

#lambda匿名函数
lambda x:x*x   #这是一个函数
f=lambda x:x*x
f(6)   #36
list(filter(lambda n:n%2 ==1,range(1,11)))   #[1, 3, 5, 7, 9]

#装饰器
import functools,time
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log   #将装饰器置于函数的定义处
def now():
    print('2015-3-25')
now()   #call now():
        #2015-3-25

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('begin call %s():' % fn.__name__)
        start=time.time()
        fn(*args,**kw)
        end=time.time()
        print('%s executed in %s ms' % (fn.__name__,end-start))
        print('end call')
    return wrapper
@metric
def fast(x,y):
    time.sleep(0.0012)
    return x+y    
fast(2,3)
'''
结果：
begin call fast():
fast executed in 0.0020024776458740234 ms
end call
'''
#转二进制
int('10111010',base=2)   #186
#functools.partial帮助创建一个偏函数，即固定已有函数的某些参数
import functools
int2=functools.partial(int,base=2)   #定义函数
int2('11010010')   #210
int2('11010010',base=8)   #2363400
#选出数列中的最大值，若小于10则输出10
max10=functools.partial(max,10)
max10(1,3,5,4)   #10

#针对二进制
#输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
5>>0   #5
[(5>>i & 1) for i in range(0,32)]   #[1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #32个
#取反 ~  按位与 &   或 |   异或 ^    左移 <<   右移 >> 

'''
外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
'''
'''
if __name__='__main__':
    function()
'''