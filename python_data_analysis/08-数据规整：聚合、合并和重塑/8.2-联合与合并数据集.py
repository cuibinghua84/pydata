# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.2-联合与合并数据集.py
@time: 2019/10/25 17:36
"""

from pprint import pprint
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 8.2.1 数据库风格的DataFrame连接
print("*" * 30)
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(df1)
print(df2)
print(df3)
print(df4)

# print(pd.merge(df1, df2))
# print(pd.merge(df1, df2, on='key'))

print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

print(pd.merge(df1, df2, how='outer'))
"""
how参数的不同连接类型
inner
left
right
outer
"""
print("*" * 30)
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'], 'data2': range(5)})
print(df1)
print(df2)
# print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, how='inner'))

print("*" * 30)
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'], 'key2': ['one', 'two', 'one'], 'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 'key2': ['one', 'one', 'one', 'two'], 'rval': [4, 5, 6, 7]})
print(left)
print(right)
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

print("*" * 30)
print(pd.merge(left, right, on='key1'))
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))
"""
merge函数参数
left
right
how
on
left_on
right_on
left_index
right_index
sort
suffixes
copy
indicator
"""

# 8.2.2 根据索引合并
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)

# 8.2.3 沿轴向连接
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)

# 8.2.4 联合重叠数据
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)
# print("*" * 30)


