# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 20:16:21 2018

@author: Administrator
"""

#模块
'''
目录结构举例：
mycompany             顶层包名
    web
        __init__.py
        utils.py      模块名：mycompany.web.utils
        www.py
    __init__.py
    abc.py
    xyz.py
'''
'''
__xxx__  类似这样的变量是特殊变量，可以被直接引用
_xxx 或 __xxx    类似这样的函数或变量是非公开的，不应该被直接引用，可以隐藏代码细节
'''
'''
在交互式环境下，搜索路径存放在sys模块的path变量中：
sys.path

如果要添加自己的搜索目录，两种办法：
1.直接修改sys.path，添加要搜索的目录：
  import sys
  sys.path.append('路径')
  这种方法是在运行时修改，运行结束后失效
2.设置环境变量PYTHONPATH
  设置方式与设置path环境变量类似。
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
    