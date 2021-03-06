# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/19 17:03
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import nan as NA
from pprint import pprint


def fs():
    print("*" * 50)


# 8.1 分层索引
data = Series(np.random.randn(9),
              index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                     [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data)
print(data.index)

fs()
print(data['b'])
print(data['b': 'c'])
print(data.loc[['b', 'd']])

fs()
print(data.loc[:, 2])

fs()
print(data)
print(data.unstack())
print(data.unstack().stack())

fs()
frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index=[['a', 'a', 'b', 'b'],
                         [1, 2, 1, 2]],
                  columns=[['Ohio', 'Ohio', 'Colorado'],
                           ['Green', 'Red', 'Green']])
print(frame)

fs()
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame['Ohio'])
print(frame['Colorado'])

# 8.1.1 重排序和层级排序
fs()
fs()
print(frame)
fs()
print(frame.swaplevel('key1', 'key2'))

fs()
print(frame.sort_index(level=1))

fs()
print(frame.swaplevel(0, 1).sort_index(level=0))

# 8.1.2 按层级进行汇总统计
fs()
print(frame.sum(level='key2'))

fs()
print(frame)
print(frame.sum(level='color', axis=1))

# 8.1.3 使用DataFrame的列进行索引
fs()
frame = DataFrame({'a': range(7), 'b': range(7, 0, -1),
                   'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)
print()
frame2 = frame.set_index(['c', 'd'])
print(frame2)

fs()
print(frame.set_index(['c', 'd'], drop=False))

fs()
print(frame2.reset_index())

# 8.2 联合与合并数据集
fs()
# 8.2.1 数据库风格的DataFrame连接
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df1)
print(df2)
print(pd.merge(df1, df2))
print(pd.merge(df1, df2, on='key'))

fs()
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df3)
print(df4)
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))

fs()
print(pd.merge(df1, df2, how='outer'))
"""
how参数的不同连接类型
inner   只对两张表都有的键的交集进行联合
left    对所有左表的键进行联合
right   对所有右表的键进行联合
outer   对两张表都有的键的并集进行联合
"""

fs()
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
print(df1)
print(df2)
print(pd.merge(df1, df2, on='key', how='left'))

fs()
print(pd.merge(df1, df2, how='inner'))

fs()
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
print(left)
print(right)
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
suffixes
copy
indicator
"""

# 8.2.2 根据索引合并
fs()
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                   'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print(right1)
print(pd.merge(left1, right1, left_on='key', right_index=True))

fs()
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))

fs()
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'enent2'])
print(lefth)
print(righth)
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))

fs()
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how='outer'))

fs()
left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                  index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8], [9., 10.], [11., 12.], [13., 14.]],
                   index=['b', 'c', 'd', 'e'],
                   columns=['Missouri', 'Alabama'])
print(left2)
print(right2)
print(pd.merge(left2, right2, how='outer', left_index=True, right_index=True))

fs()
print(left2.join(right2, how='outer'))

fs()
print(left1.join(right1, on='key'))

fs()
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'],
                    columns=['New York', 'Oregon'])
print(another)
print(left2.join([right2, another]))
print(left2.join([right2, another], how='outer'))

# 8.2.3 沿轴向连接
fs()
arr = np.arange(12).reshape((3, 4))
pprint(arr)
pprint(np.concatenate([arr, arr], axis=1))

fs()
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
print(s1)
print(s2)
print(s3)
print(pd.concat([s1, s2, s3]))
print(pd.concat([s1, s2, s3], axis=1, sort=True))

fs()
s4 = pd.concat([s1, s3])
print(s4)
print(pd.concat([s1, s4], axis=1, sort=True))
print(pd.concat([s1, s4], axis=1, join='inner', sort=True))
# print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))

fs()
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print(result.unstack())

fs()
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'], sort=True))

fs()
df1 = DataFrame(np.arange(6).reshape((3, 2)),
                index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape((2, 2)),
                index=['a', 'c'],
                columns=['three', 'four'])
print(df1)
print(df2)
print(pd.concat([df1, df2], axis=1, keys=['leval1', 'level2'], sort=True))

fs()
print(pd.concat({'level1': df1, 'level2': df2}, axis=1, sort=True))

fs()
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
                names=['upper', 'lower'], sort=True))

fs()
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
print(df1)
print(df2)
print(pd.concat([df1, df2], ignore_index=True, sort=True))
"""
concat函数的参数
objs
axis
join
join_axes
keys
leels
"""

fs()
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})
print(df1)
print(df2)
print(df1.combine_first(df2))

# 8.2.4 联合重叠数据
fs()
a = Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series([0., np.nan, 2., np.nan, np.nan, 5.],
           index=['a', 'b', 'c', 'd', 'e', 'f'])
print(a)
print(b)
print(pd.isnull(a))
print(np.where(pd.isnull(a), b, a))

# 8.3 重塑和透视
# 8.3.1 使用多层索引进行重塑
fs()
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'],
                                  name='number'))
print(data)

fs()
result = data.stack()
print(result)

fs()
print(result.unstack())

fs()
print(result.unstack(0))

fs()
print(result.unstack('state'))

fs()
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print(s1)
print(s2)
print(data2)
print(data2.unstack())

fs()
print(data2.unstack())

fs()
print(data2.unstack().stack())

fs()
print(data2.unstack().stack(dropna=False))

fs()
df = DataFrame({'left': result, 'right': result +5},
               columns=pd.Index(['left', 'right'], name='side'))
print(df)

fs()
print(df.unstack('state'))

fs()
print(df.unstack('state').stack('side'))

# 8.3.2 将“长”透视为“宽”
fs()
data = pd.read_csv('D:/data/pydata_book2/examples/macrodata.csv')
print(data.head())

fs()
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='data')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata[:10])

fs()
pivoted = ldata.pivot('data', 'item', 'value')
print(pivoted)

fs()
ldata['value2'] = np.random.randn(len(ldata))
print(ldata[:10])

fs()
pivoted = ldata.pivot('data', 'item')
print(pivoted[:5])
print(pivoted['value'][:5])

fs()
unstacked = ldata.set_index(['data', 'item']).unstack('item')
print(unstacked[:7])

# 8.3.3 将“宽”透视为“长”
fs()
df = DataFrame({'key': ['foo', 'bar', 'baz'],
                'A': [1, 2, 3],
                'B': [4, 5, 6],
                'C': [7, 8, 9]})
print(df)

fs()
melted = pd.melt(df, ['key'])
print(melted)

fs()
reshaped = melted.pivot('key', 'variable', 'value')
print(reshaped)

fs()
print(reshaped.reset_index())

fs()
print(pd.melt(df, id_vars=['key'], value_vars=['A', 'B']))

fs()
print(pd.melt(df, value_vars=['A', 'B', 'C']))

print(pd.melt(df, value_vars=['key', 'A', 'B']))