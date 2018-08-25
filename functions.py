# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 08:11:23 2018

@author: Administrator
"""
#python内置函数
#https://docs.python.org/3/library/functions.html

#字符串的连接

'22'+'44'   #'2244'
list(map(int,'22'+'44'))   #[2, 2, 4, 4]

#拥有相同值的list的生成

[[0 for _ in range(4)] for _ in range(3)]   #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
[0]*3*4   #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#逻辑判断，只能放一个iterable（例如：一个list）
#如果对象含有元素0、''、False或者为空对象，都会返回False

all([0,'',1])   #False
all([3<2,2<3,3<4])   #False
all([1,2,3])   #True

#如果对象含有0、''、False或者为空对象之外的原素，就会返回True

any([0,'',1])   #True
any([3<2,2<3,3<4])   #True
any([1,2,3])   #True

#返回一个可打印的string

ascii('成')   #"'\\u6210'"
print(ascii('abc'))   #'abc'
print('abc')          #abc

#输出前缀为0b的二进制

bin(3)   #'0b11'
format(3,'#b'),format(3,'b')   #('0b11', '11')
f'{3:#b}',f'{3:b}'   #('0b11', '11')
       
#布尔值

print(bool(1))   #True
print(bool(1>2))   #False
'''
以下会被判定为False：
1. None
2. False
3. 任何包含0的数字形式，例如0，0.0，0j
4. 任何空的序列，例如'',(),[]
5. 任何空的映射，例如{}
6. 用户自己定义的类中的__bool__()或者__len__()方法返回0或者False
'''
print(bool([3<2,3>2]))   #True
print(bool([3<2,3>4]))   #True

True + True + True   #3

#查看对象是否可调用，callable(object)，例如对象是一个已定义的方程时，返回True

#
chr(97)   #'a'
ord('a')   #97

#删除属性，同setattr()反义
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

#赋属性

fn=getattr(obj,'power')
fn()   #81
#同
obj.power()   #81

#删除属性

delattr(obj,'y')
hasattr(obj,'y')   #False

#返回class中的所有属性名称：dir()

#同时返回整除个数和余数

divmod(2,3)   #(0, 2)
divmod(2,3)[0]   #0 

#遍历同时加上序号

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons,start=1))   #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

#返回数值

eval('4.5')   #4.5   type后为float
eval('1+7')   #8     type后为int

#同返回，但是可以有多行代码

x=10
expr=r'''
z=30
sum=x+y+z
print(sum)'''   #多行代码放入exec()，必须有print，否则只会返回None，每行前面不能有空格
def func():
    y=20
    exec(expr)                               #10+20+30
    exec(expr,{'x':1,'y':2})                 #1+2+30
              #  全局变量    局部变量区（不改全局变量z）
    exec(expr,{'x':1,'y':2},{'y':3,'z':4})   #1+3+30
func()   #60 33 34

#repr()同返回，但是针对string

a='成'
repr=r'''
c='岩'
name=a+b+c
print(name)'''
def func_name():
    b='岩'
    exec(repr)
    exec(repr,{'a':'张', 'b':''})
func_name()

#正则

'Good {0}, {1}! {1} is here.'.format('moring','Yan')   #'Good moring, Yan! Yan is here.'

#hash()返回哈希值

pow(5,2)   #25   5**2

#倒序

list(reversed(['a','b','c']))   
list(reversed(str(123)))   #['3', '2', '1']
list(str(123)[::-1])   #['3', '2', '1']

#组合，解压

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)  # 打包为元组的列表  [(1, 4), (2, 5), (3, 6)]
zip(a,c)           # 元素个数与最短的列表一致  [(1, 4), (2, 5), (3, 6)]  
zip(*zipped)       # 与 zip 相反，可理解为解压，返回二维矩阵式  [(1, 2, 3), (4, 5, 6)]


from datetime import datetime

now=datetime.now()
print(now)   #2018-04-05 14:27:59.750513

#指定时间

dt=datetime(2018,4,1,14,40)

#转换为数字

dt.timestamp()   #1522564800.0

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%l 12小时制小时数（01-12）
%M 分钟数（00-59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

#str转时间

cday=datetime.strptime('2018-4-1 20:00:00','%Y-%m-%d %H:%M:%S')
print(cday)    #2018-04-01 20:00:00

#时间转str

print(now.strftime('%a, %b %d %H:%M'))   #Thu, Apr 05 14:27

#时间加减

from datetime import datetime,timedelta
datetime.now()+timedelta(hours=10)   #datetime.datetime(2018, 4, 6, 0, 38, 40, 933208)
datetime.now()+timedelta(days=2,hours=10) #datetime.datetime(2018, 4, 8, 0, 39, 17, 398903)

#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
#以及一个时区信息如UTC+5:00，均是str，
#请编写一个函数将其转换为timestamp：
import re
from datetime import timezone
def to_timestamp(dt_str, tz_str):
    t = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    u = re.match(r'UTC([\+\-]\d+):[\d]+',tz_str).group(1)
    tt = t.replace(tzinfo=timezone(timedelta(hours=float(u))))
    return tt.timestamp()

#获取日历
#https://www.cnblogs.com/zhangxinqi/p/7687862.html
    
import calendar
cal=calendar.month(2018,9)
print(cal)
'''
   September 2018
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
'''

c=calendar.calendar(2018)
print(c)
'''
                                  2018

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
29 30 31                  26 27 28                  26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1          1  2  3  4  5  6                   1  2  3
 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                      1  2
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                      1  2
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
                                                    31
'''

                                                    