# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 16:33:59 2018

@author: Administrator
"""
#file:///E:/Python_project/第五讲/part2.html#钱晨
import pandas

#基础IO工具

'''
读写CSV文件
pandas.read_csv(filepath,header,names,skiprows,encoding)
其中：header: int(指CSV文件中的第几行)
      names: arrary like(list等) 如果header=None，接受names传入
      skiprows:int

读写xlsx文件
pandas.read_excel(filepath,sheetname,header,names,skiprows)

数据类型：
series：一维数据，可以容纳不同数据类型和数据标签
dataframe：二维数据
paneldata：面板数据
'''
