# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.1-note.py
@time: 2019/11/18 11:41
"""

import numpy as np
import pandas as pd
from pprint import pprint
from pandas import DataFrame, Series


def fs():
    print("*" * 40)


# 8.1 分层索引
# 分层索引提供了一种在更低维度的形式中处理更高维度数据的方式
data = pd.Series(np.random.randn(9), index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                                            [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data)
print(data.index)

fs()
print(data['b'])
print(data['b': 'c'])
# loc通过行标签索引数据
# iloc通过行号获取数据，不能是字符
print(data.loc[['b', 'd']])

fs()
print(data.loc[:, 2])

fs()
print(data.unstack())
print(data.unstack().stack())

fs()
frame = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'],
                                                           [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
print(frame)

fs()
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
pprint(frame)
print(frame['Ohio'])

# 8.1.1 重排序和层级排序
fs()
print(frame)
print(frame.swaplevel('key1', 'key2'))
print(frame.sort_index(level=1))
print(frame.swaplevel(0, 1).sort_index(level=0))

# 8.1.2 按层级进行汇总统计
fs()
fs()
print(frame)
fs()
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))

# 8.1.3 使用DataFrame的列进行索引
fs()
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
frame2 = frame.set_index(['c', 'd'])
print(frame)
print(frame2)
print(frame.set_index(['c', 'd'], drop=False))
print(frame2.reset_index())
