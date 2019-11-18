# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.2-note.py
@time: 2019/11/18 11:42
"""

import numpy as np
import pandas as pd
from pandas import DataFrame, Series


def fs():
    print("*" * 40)


# 8.2 联合与合并数据集
# 8.2.1 数据库风格的DataFrame连接
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print(df2)
print(pd.merge(df1, df2))

fs()
print(pd.merge(df1, df2, on='key'))

fs()
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

fs()
print(pd.merge(df1, df2, how='outer'))
"""
how参数的不同连接类型
inner
left
right
outer
"""

fs()
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})
print(df1)
print(df2)
print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, how='inner'))

fs()
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})
print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))

fs()
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

# 8.2.2根据索引合并
fs()
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print(right1)
print(pd.merge(left1, right1, left_on='key', right_index=True))

fs()
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))

fs()
lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)), index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                                                            [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['enent1', 'enent2'])
print(lefth)
print(righth)

# 8.2.3 沿轴向连接

# 8.2.4 联合重叠数据


