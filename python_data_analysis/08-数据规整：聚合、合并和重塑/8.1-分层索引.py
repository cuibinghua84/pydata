# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.1-分层索引.py
@time: 2019/10/25 17:36
"""

from pprint import pprint
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 3, 1, 2, 2, 3]])
pprint(data)
# pprint(data.index)
# print(data['b'])
# print(data['b':'c'])
# print(data.loc[['b', 'd']])
# print(data.loc[:, 2])

print("*" * 20)
print(data.unstack())
print(data.unstack().stack())

print("*" * 20)
frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
pprint(frame)

print("*" * 20)
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame['Ohio'])

# 8.1.1 重排序和层级排序
print("*" * 30)
print(frame.swaplevel('key1', 'key2'))

print("*" * 30)
print(frame.sort_index(level=1))

print("*" * 30)
print(frame.swaplevel(0, 1).sort_index(level=0))

# 8.1.2 按层级进行汇总统计
print("*" * 30)
print(frame.sum(level='key2'))

print("*" * 30)
print(frame.sum(level='color', axis=1))

# 8.1.3 使用DataFrame的列进行索引
print("*" * 30)
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)

print("*" * 30)
frame2 = frame.set_index(['c', 'd'])
print(frame2)

print("*" * 30)
print(frame.set_index(['c', 'd'], drop=False))

print("*" * 30)
print(frame2.reset_index())

print("*" * 30)

