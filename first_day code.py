# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 18:15:36 2019

@author: Administrator
"""

'''
1.二维数组中的查找

在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''
#思路：从左下角开始考虑，如果给定整数比该数大，则右移比较；如果比该数小，则左移比较。若从左上角开始，则存在分叉，无法确定向下或向右。

#按照思路解法（原创）（适合python2）
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        result='false'
        i=len(array)-1
        j=0
        while i>=0 and j<len(array[0]):
            com=array[i][j]
            if target == com:
                result='true'
                break
            if target < com:
                i=i-1
            else:
                j=j+1
        return result
while True:
    try:
        s=Solution()
        a=list(eval(raw_input()))
        target=a[0]
        array=a[1]
        print(s.Find(target,array))
    except:
        break
    
#简便解法（适合python2）
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        result='false'
        for i in range(len(array)):
            if target in array[i]:
                result='true'
                break
        return result
while True:
    try:
        s=Solution()
        a=list(eval(raw_input()))
        target=a[0]
        array=a[1]
        print(s.Find(target,array))
    except:
        break
    
#笔记：
        
#检查list中是否含有某元素时，使用
if 2 in [1,2,3]:
    print('true')
    
#关于错误调试
while True:
    try:
        #写上调用class的各个步骤
    except:
        break
    
#关于raw_input()
#在python2中，raw_input()将输入的内容自动变为字符串格式，而input()不会改变输入内容的格式
#在python3中，input()代替了2中的raw_input()
a=input('Please input your name: ')
#输入10时，a的输出结果为"10";输入'10'时，a的输出结果为"'10'"
#将输入的10变为数值型
int(a)

#做题时，python2和3的不同输入格式
#python2
a=list(eval(raw_input()))
print(a[0],a[1])
#python3
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


'''
2.替换空格

请实现一个函数，
将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
'''
#思路：从前向后遍历，从后向前替换？？

#解法1：
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return '%20'.join(list(s.split(' ')))

#解法2：
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        ss=''
        for i in s:
            if i==' ':
                ss=ss+'%20'
            else:
                ss=ss+i
        return ss
    
#解法3：
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ','%20')
    
#笔记：字符串的拆分与组合