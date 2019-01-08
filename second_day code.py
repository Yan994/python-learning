# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:24:17 2019

@author: Administrator
"""

'''
3.从尾到头打印链表

输入一个链表，
按链表值从尾到头的顺序返回一个ArrayList。
'''
#思路：递归，栈。先列出链表值，在反转列表

# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        l=[]
        while listNode:
            l.append(listNode.val)
            listNode=listNode.next
            #此处改变了listNode的原始值，所以循环有尽头
        l.reverse()
        #return list(reversed(l))
        return l
    
#笔记：
        
#求列表反转：
a=[1,2,3]
b=a
aa=a
aaa=a[:]  #此时a与aaa的操作互不干扰
#法一（a的内容也被改变了，aaa没变）：
b.reverse()
print(b)  #[3, 2, 1]
print(a)  #[3, 2, 1] 
print(aa) #[3, 2, 1]
print(aaa)#[1, 2, 3]
#法二（栈的思想）（a的内容及a定义过去的b和aa都改变了）：
c=[]
while a:
    c.append(a.pop())
print(c)  #[1, 2, 3]
print(a)  #[]
print(b)  #[]
print(aa) #[]
print(aaa)#[1, 2, 3]
#法三（切片）：
print(aaa[::-1])  #[3, 2, 1]
print(a)          #[]


'''
4.重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，
请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中
都不含重复的数字。
例如输入前序遍历序列
{1,2,4,7,3,5,6,8}
和中序遍历序列
{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
'''
#思路：前序中的为节点root，中序中以节点分左右。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        else:
            r=TreeNode(pre.pop(0))
            i=tin.index(r.val)
            r.left=self.reConstructBinaryTree(pre[:i],tin[:i])
            r.right=self.reConstructBinaryTree(pre[i:],tin[i+1:])
            return r
        
#笔记：
            
#对函数的调用形式
            
#二叉树
#设L、D、R分别表示遍历左子树、访问根结点和遍历右子树，
#DLR（先根次序遍历），LDR（中根次序遍历），LRD （后根次序遍历）。
   
        
'''
5.用两个栈实现队列

用两个栈来实现一个队列，
完成队列的Push和Pop操作。
队列中的元素为int类型。
'''
#思路：队列：先入先出；栈：先入后出
#传统的append后的pop是先入后出，是栈
#现在要建立函数使用pop实现先入先出
#l1为栈1，表示队列的后半部分，实现入
#l2为栈2，表示队列的前半部分，实现出

#解法一：两个栈实现
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l1=[]
        self.l2=[]
    def push(self,node):
        self.l1.append(node)
    def pop(self):
        if self.l1 and not self.l2 :
            while self.l1:
                self.l2.append(self.l1.pop())
        return self.l2.pop()
    
#解法二：一个栈实现（其实不符合题意）
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l=[]
    def push(self,node):
        self.l.append(node)
    def pop(self):
        while self.l:
            return self.l.pop(0)        