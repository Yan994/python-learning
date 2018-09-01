# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:18:37 2018

@author: Administrator
"""
import numpy as np
from pandas import Series,DataFrame
import pandas as pd


#series

obj=Series([4,7,-5,3])
print(obj)
'''
0    4
1    7
2   -5
3    3
dtype: int64
'''
#series的字符串表现形式为：索引在左边，值在右边。由于我们没有指定索引，所以自动创建0到n-1的整数型索引。

obj.values
#array([ 4,  7, -5,  3], dtype=int64)
obj.index
#RangeIndex(start=0, stop=4, step=1)

obj2=Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)
'''
d    4
b    7
a   -5
c    3
dtype: int64
'''
obj2.index
#Index(['d', 'b', 'a', 'c'], dtype='object')
obj2['c']
#3
obj2['d']=6   #改变该索引对应的值
obj2[['d','a']]
'''
d    6
a   -5
dtype: int64
'''

#无论做什么计算，索引始终跟着

obj2[obj2>0]   #选择部分数据
'''
d    6
b    7
c    3
dtype: int64
'''
obj*2   #对数据做运算
'''
0     8
1    14
2   -10
3     6
dtype: int64
'''
np.exp(obj2)
'''
d     403.428793
b    1096.633158
a       0.006738
c      20.085537
dtype: float64
'''
'b' in obj2
#True

#当存在一个python字典时，可以直接创建series

sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=Series(sdata)
print(obj3)
'''
Ohio      35000
Texas     71000
Oregon    16000
Utah       5000
dtype: int64
'''

#如果传入指定索引，则被指定的索引就按照原字典的键对应值

states=['California','Ohio','Oregon','Texas']
obj4=Series(sdata,index=states)
print(obj4)
'''
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
'''

#检测缺失数据

pd.isnull(obj4)
'''
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
'''
pd.notnull(obj4)
'''
California    False
Ohio           True
Oregon         True
Texas          True
dtype: bool
'''
obj4.isnull()
'''
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
'''

#series之间的运算会自动对齐不同索引的数据

print(obj3+obj4)
'''
California         NaN
Ohio           70000.0
Oregon         32000.0
Texas         142000.0
Utah               NaN        有一个空值求和后还是空值
dtype: float64
'''

#series对象本身及其索引的name属性

obj4.name='population'
obj4.index.name='state'
print(obj4)
'''
state
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
Name: population, dtype: float64
'''

#索引可以通过赋值的方式改变

obj.index=['Bob','Steve','Jeff','Ryan']
print(obj)
'''
Bob      4
Steve    7
Jeff    -5
Ryan     3
dtype: int64
'''



#dataframe
#可以被看做由series组成的字典，共用同一个索引

#构建dataframe

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
print(frame)
'''
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2    Ohio  2002  3.6
3  Nevada  2001  2.4
4  Nevada  2002  2.9
'''
#自动加上了索引

#如果指定了列序列，则DataFrame的列就会按照指定顺序进行排列

DataFrame(data,columns=['year','state','pop'])
'''
   year   state  pop
0  2000    Ohio  1.5
1  2001    Ohio  1.7
2  2002    Ohio  3.6
3  2001  Nevada  2.4
4  2002  Nevada  2.9
'''

#如果传入的列在数据中找不到，就会产生NA值

frame2=DataFrame(data,columns=['year','state','pop','debt'],
                 index=['one','two','three','four','five'])
print(frame2)
'''
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN
'''
print(frame2.columns)
#Index(['year', 'state', 'pop', 'debt'], dtype='object')

#提取列

print(frame2['state'])
print(frame2.year)

#提取行

print(frame2.loc['three'])
'''
year     2002
state    Ohio
pop       3.6
debt      NaN
Name: three, dtype: object
'''

#给列赋值

#赋相同固定值

frame2['debt']=16.5
print(frame2)
'''
       year   state  pop  debt
one    2000    Ohio  1.5  16.5
two    2001    Ohio  1.7  16.5
three  2002    Ohio  3.6  16.5
four   2001  Nevada  2.4  16.5
five   2002  Nevada  2.9  16.5
'''

#赋数列

frame2['debt']=np.arange(5)
print(frame2.debt)
'''
one      0
two      1
three    2
four     3
five     4
Name: debt, dtype: int32
'''

#赋选定值，长度必须跟DataFrame的长度相匹配，空位将被填上缺失值

val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
print(frame2)
'''
       year   state  pop  debt
one    2000    Ohio  1.5   NaN
two    2001    Ohio  1.7  -1.2
three  2002    Ohio  3.6   NaN
four   2001  Nevada  2.4  -1.5
five   2002  Nevada  2.9  -1.7
'''

#为不存在的列赋值会创建出一个新列

frame2['eastern']=frame2.state=='Ohio'
print(frame2)
'''
       year   state  pop  debt  eastern
one    2000    Ohio  1.5   NaN     True
two    2001    Ohio  1.7  -1.2     True
three  2002    Ohio  3.6   NaN     True
four   2001  Nevada  2.4  -1.5    False
five   2002  Nevada  2.9  -1.7    False
'''

#删除列

del frame2['eastern']
print(frame2.columns)
#Index(['year', 'state', 'pop', 'debt'], dtype='object')

#通过索引方式返回的列只是相应数据的视图，并不是副本。对其的修改会反映到源dataframe上。



#嵌套字典（字典的字典）

pop={'Nevada':{2001:2.4, 2002:2.9},
     'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
frame3=DataFrame(pop)
print(frame3)
'''
      Nevada  Ohio
2000     NaN   1.5
2001     2.4   1.7
2002     2.9   3.6
'''
#外层字典的键为列，内层键为索引

#转置

print(frame3.T)
'''
        2000  2001  2002
Nevada   NaN   2.4   2.9
Ohio     1.5   1.7   3.6
'''

#指定嵌套字典的键
 
#frame4=DataFrame(pop, index=[2001, 2002, 2003])
#出不来结果，可能版本问题