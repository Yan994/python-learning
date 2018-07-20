# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:41:26 2017

@author: Administrator
"""
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
组成所有的排列后再去掉不满足条件的排列。
'''
#程序源代码
for i in range(6):     #6代表从0开始走6个数，0,1,2,3,4,5
      print i
 
for i in range(1,5):   #1代表从1开始，5代表从0开始走5个数到4结束
      for j in range(1,5):
            for k in range(1,5):
                  if (i!=j) and (i!=k) and (j!=k):
                        print i*100+j*10+k

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
i=int(raw_input('净利润：'))
arr=[1000000,600000,400000,200000,100000,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for idx in range(6):
      if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print (i-arr[idx])*rat[idx]
            i=arr[idx]
print r
#没有结果
'''
题目：暂停一秒输出。
'''
import time                      #用途，定时执行程序
myD={1:'a',2:'b'}
for key,value in dict.items(myD):
      print key,value
      time.sleep(1)    #程序暂停一秒
      
'''
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''
score=int(raw_input('输入分数:\n'))
if score>=90:
      grade='A'
elif score>=60:
      grade='B'
else: grade='C'
print '%d 属于 %s' % (score,grade)

'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
tour=[]
height=[]

hei=100   #起始高度
tim=10   #落地次数

for i in range(1,tim+1):
      if i==1:
            #从第二次开始，落地时的距离是反弹高度乘以2
            tour.append(hei)
      else:tour.append(hei*2)
      hei=float(hei)/float(2)    #返回hei为hei除以2
      #原代码：hei /= 2    返回hei为hei除以2后的取整
      height.append(hei)
      
print ('总高度：tour={0}'.format(sum(tour)))
print ('第十次反弹高度：height={0}'.format(height[-1]))#-1代表倒数第一个数值

#List
#新建列表
testList=[10086,'中国移动',[1,2,4,5]]
#访问列表长度
print len(testList)    #结果为3,两个逗号隔开的三个
#到列表结尾
print testList[1:]    #输出第2及以后内容
#向列表添加元素
testList.append('i\'m new here!') #加上\符号表示后面引号‘是引号内容中的内容

print testList.pop(1)    #输出列表中将被删除的第二个元素


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print matrix
print matrix[1]   #输出第二行
col2=[row[1] for row in matrix]  #每行取第二个数值，构成矩阵第二列
print col2
col2even=[row[1] for row in matrix if row[1]%2==0]
print col2even                           #偶数
            
