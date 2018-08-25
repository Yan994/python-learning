# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:54:33 2018

@author: Administrator
"""

#创建数组
tup="a","b","c","d"
tup_sig='a','b','c','d'
print(tup)  #('a', 'b', 'c', 'd')
print(tup_sig)   #('a', 'b', 'c', 'd')

#传参（必须双引号）
print("{name}元组的第一个元素是{value}".format(name='tup',value=tup[0]))

print(tup.index('c'))

import datetime
now=datetime.datetime.now()
print(now)
now_str=str(now)
print(now_str)
#删去后10位
print(now_str[:-10])

#获取时间
now=str(datetime.datetime.now())
print(now) #2018-08-21 20:02:20.009007

print(now[:19]) #2018-08-21 20:02:20

#获取昨天的时间
yesterday=(datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y%m%d')
print(datetime.date.today())  #2018-08-21
print(yesterday)  #20180820

type(yesterday)

import pymysql
import datetime
#获取连接对象【配置连接的界面】
conn=pymysql.connect(host='airflow.bigdata.zichan360.com',
                     port=3306,
                     user='***********@zichan360.com',
                     passwd='coY9HXwbxq9jzH',
                     db='zichan360bi_temp',
                     charset='utf8')
#获取游标【相当于打开查询界面】
cur=conn.cursor()
#定义sql
sql='''
    SELECT
      client_company_id,
      agent_company_id,
      case_overdue_day
    FROM
      zichan360bi_temp.agent_rate_new_yxc
    WHERE
      date(dat_rcd_dt) = '{yesterday}'
    LIMIT 100;
    '''.format(yesterday=(
    datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
#执行查询
cur.execute(sql)
#获取查询结果
table_info=cur.fetchall()
#取一行数据
row_one=cur.fetchone()
#取几行数据
row_many=cur.fetchmany(3)
#展示结果
print(table_info)
'''
((2778, 2148, 181), (2778, 2452, 181), (2778, 4482, 181), (2778, 4643, 181), (2778, 5296, 181), (2778, 5456, 181), (2778, 5473, 181), (2778, 5569, 181), (2778, 5629, 181), (2778, 3939, 361), (2778, 4245, 361), (2778, 4642, 361), (2778, 5422, 361), (2954, 5019, 211), (2954, 4607, 271), (2954, 5312, 361), (2956, 4785, 1), (2956, 4785, 1), (2956, 4785, 1), (2956, 5219, 31), (2956, 3417, 121), (2956, 3417, 211), (2956, 4607, 331), (2956, 5467, 361), (2957, 5467, 361), (2976, 2856, 1), (2976, 5219, 181), (2991, 3656, 1), (2991, 3656, 1), (2991, 3656, 1), (2991, 3656, 1), (2991, 3656, 11), (2991, 3656, 11), (2991, 3315, 31), (2991, 5596, 61), (2991, 5308, 91), (2991, 3198, 361), (2993, 5330, 211), (3002, 3930, 1), (3002, 3930, 1), (3002, 3930, 1), (3002, 2864, 11), (3002, 3417, 121), (3002, 5474, 331), (3006, 4785, 1), (3006, 3417, 91), (3006, 5568, 121), (3006, 3417, 181), (3007, 4785, 1), (3007, 4785, 1), (3007, 4291, 11), (3007, 2500, 61), (3007, 5312, 211), (3008, 5357, 121), (3008, 2856, 181), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 2852, 1), (3013, 4785, 11), (3013, 4785, 11), (3013, 3448, 31), (3013, 4785, 31), (3013, 5602, 31), (3013, 3315, 61), (3013, 5596, 61), (3013, 3417, 121), (3013, 3417, 151), (3013, 3417, 181), (3031, 3930, 1), (3031, 3930, 1), (3031, 3930, 1), (3033, 4785, 1), (3033, 4785, 1), (3033, 4785, 1), (3033, 5602, 11), (3037, 2935, 1), (3037, 5219, 61), (3037, 2500, 181), (3039, 2867, 1), (3039, 5474, 181), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1), (3045, 2869, 1))
'''
#关闭游标
cur.close()
#关闭连接
conn.close()



print(type(table_info))
#<class 'tuple'>

print(len(table_info))
#100

list_test=list(table_info[0])

#删除特定位置的元素
del list_test[1]
print(list_test)
#删除特定元素
list_test.remove(181)
print(list_test)   #[2778]

list_test=list(table_info[0])
print(list_test)   #[2778, 2148, 181]
#反转
print(list(reversed(list_test)))
list_test.reverse()
print(list_test)   #[181, 2148, 2778]
#降序
print(list(sorted(list_test)))
list_test.sort(reverse=True)
print(list_test)   #[2778, 2148, 181]

#获取每一行数据所对应的行号，数据来源除了数据库也可以是Excel，索引为0的是表格第二行（数据第一行）
num=[0,1,2]
#循环
print([i+2 for i in num])
#[2,3,4]

#定义函数
def add_2(t):
    t+=2
    return t
print(list(map(add_2,num)))
#[2,3,4]

#匿名函数
print(list(map(lambda i:i+2, num)))
#[2,3,4]

