# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.2-基本功能.py
@time: 2019/10/16 9:34
"""

from pprint import pprint
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 5.2.1 重建索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6])
print(obj)
print("重建索引")
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

print("\n")
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

print("\n")
obj3 = pd.Series(['bule', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)

print("\n")
print(obj3.reindex(range(6), method='ffill'))

print("\n")
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['0hio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

print("\n")
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
"""
reindex方法的参数
index：新建作为索引的序列，可以是索引实例或任意其他序列型Python数据结构，索引使用时无需复制
"""

print("\n")
print(frame.loc[['a','b', 'c', 'd'], states])

# 5.2.2 轴向上删除目录
print("\n")
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'c']))

print("\n")
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['0hio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data)

print("\n")
print(data.drop(['Colorado', '0hio']))

print("\n")
print(data.drop('two', axis=1))

print("\n")
obj.drop('c', inplace=True)
print(obj)

# 5.2.3 索引、选择与过滤
print("\n")
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

print("\n")
print(obj['b': 'c'])
obj['b':'c'] = 5
print(obj)

print("\n")
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['0hio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])
print(data[:2])
print(data[data['three'] > 5])

print("\n")
print(data < 5)
data[data < 5] = 0
print(data)

# 5.2.3.1 使用loc和iloc选择数据
print("\n")
print(data.loc['Colorado', ['two', 'three']])

print("\n")
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
print(data.iloc[[1, 2], [3, 0, 1]])

print("\n")
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])

"""
DataFrame索引选项
df[val]：从DataFrame 		选取单列或一组列；在特殊情况下比较便利；布尔型数组(过滤)、切片（行切片）、或布尔型DataFrame（根据条件设置值）
df.loc[val]： 				通过标签，选取DataFrame的单个行或一组房
df.loc[;, val]： 			通过标签，选取单列或列子集
df.loc[val1, val2]： 		通过标签，同时选取行和列
df.iloc[where]： 			通过整数位置，从DataFrame选取单个行或行子集
df.iloc[;, where]： 			通过整数位置，从DataFrame选取单个列或列子集
df.iloc[where_i, where_j]： 通过整数位置，同时选取行和列
df.at[label_i, label_j]： 	通过行和列标签，选取单一的标量
df.iat[i, j]： 				通过行和列的位置（整数），选取单一的标量
reindex： 					通过标签选取行或列
get_value,set_value： 		通过行和列标签选取单一值

"""

# 5.2.4 整数索引
print("\n")
ser = pd.Series(np.arange(3.))
print(ser)

# print("\n")

# print("\n")

# print("\n")

# 5.2.5 算术和数据对齐
# print("\n")

# print("\n")

# print("\n")

# print("\n")

# 5.2.5.1 使用填充值的算术方法
# print("\n")

# print("\n")

# print("\n")

# print("\n")

# 5.2.5.2 DataFrame和Series间的操作
# print("\n")

# print("\n")

# print("\n")

# print("\n")

# 5.2.6 函数应用和映射
# print("\n")

# print("\n")

# print("\n")

# print("\n")

# 5.2.7 排序和排名
# print("\n")

# print("\n")

# print("\n")

# print("\n")

# 5.2.8 含有重复标签的轴索引
# print("\n")

# print("\n")

# print("\n")

# print("\n")

