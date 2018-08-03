# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:38:55 2018

@author: Administrator
"""

#list

classmate=['成','小','岩']
classmate[0]   #成
classmate[-1]   #岩

#加元素

classmate.append('大')   

#指定位置加元素

classmate.insert(0,'大')

#删指定位置元素

classmate.pop(-1)

#替换

classmate[0]='小'
classmate[:3]   #['小', '成', '小']
classmate[-2:]   #['小', '岩']
classmate[:4:2]   #['小', '小']  后面2表示每两个取一个

#list可以包含各种数据类型

l=['a',1,['b','c',2],True]
len(l)    #4
l[2][2]   #2



#循环

for name in classmate:
    print(name)
#同
[name for name in classmate]



#tuple元组   定以后不可更改

#只有一个元素时，为防歧义要这样写
t=(1,)   

#元组中的list可以更改

t=(1,2,['a',1])
t[2][1]='b'



#dict字典

d={'a':1,'b':2,'c':3}
print(d['b'])   #2
d['d']=4
'e' in d   #False

#如果key不存在，可以返回None，或者自己指定的value

d.get('e',5)   #5

#删除key

d.pop('a')

#迭代key

for key in d:
    print(key)
    
#迭代value
    
for v in d.values():
    print(v)
    
#迭代所有
    
for k,v in d.items():
    print(k,'=',v)
    
    
    
#set 一组key的集合，但不存储value
    
s=set([1,2,3,3,2,2,4])
s   #{1, 2, 3, 4}

#添加元素

s.add(5)

#删除

s.remove(3)

#交并集

s1=set([1,2,3])
s2=set([2,3,4])
s1 & s2   #{2,3}
s1 | s2   #{1, 2, 3, 4}



#关于不可变对象

#list可变，内容可变

a=['c','b','a']
a.sort()   
a   #['a', 'b', 'c']

#str不可变，dict,set中的key不可变

a='abc'
a.replace('a','b')   #'bbc'
a   #'abc'

list(range(5))   # [0, 1, 2, 3, 4]



#条件判断

height=input('your height:')
weight=input('your weight:')
h=float(height)
w=float(weight)
bmi=w/h**2   #平方用**
em='您的BMI指数为%.2f，身体状况为%s。'
if bmi>32:
    print(em % (bmi,'严重肥胖'))
elif bmi>28:
    print(em % (bmi,'肥胖'))
elif bmi>25:
    print(em % (bmi,'过重'))
elif bmi>18.5:
    print(em % (bmi,'正常'))
else:
    print(em % (bmi,'过轻'))



#遍历
    
sum=0
for x in range(101):
    sum+=x   #sum=sum+x
print(sum)



#循环

sum=0
n=100
while n>0:
    sum+=n
    n-=1
print(sum)

#break 提前结束循环
#continue 跳过某些循环

n=0
while n<100:
    n+=1
    if n%2==0:
        continue
    print(n)
print('end')

n=1
while n<100:
    if n>10:
        break
    print(n)
    n+=1
