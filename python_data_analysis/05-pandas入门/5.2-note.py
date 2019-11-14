# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.2-note.py
@time: 2019/11/13 9:20
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint

# 5.2.1 重建索引
# reindex用于创建一个符合新索引的新对象
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

# ffill会将值向前填充
print("*" * 40)
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))

# reindex可以同时改变行索引、列索引
# reindex方法的参数：index=》新建作为索引的序列，可以是索引实例或任意其他序列型Python数据结构，索引使用时无需复制
print("*" * 40)
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

# 使用columns重建索引
print("*" * 40)
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))

print("*" * 40)
print(frame.loc[['a', 'b', 'c', 'd'], states])

# 5.2.2 轴向上删除条目
print("*" * 40)
# drop方法会返回一个含有指标值或轴向上删除值的新对象
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'c']))

# DataFrame索引值可以从轴向上删除
print("*" * 40)
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'California', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.drop(['California', 'Ohio']))

# 传递axis=1或axis='columns' 从列中删除值
print("*" * 40)
print(data)
print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis='columns'))

# 修改Series和DataFrame的尺寸或形状
print("*" * 40)
obj.drop('c', inplace=True)
pprint(obj)

# 5.2.3 索引、选择与过滤
# Series的索引值不仅仅是整数
print("*" * 40)
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

# 普通Python切片中不包含尾部，Series的切片则不同
print("*" * 40)
print(obj['b': 'c'])

obj['b': 'c'] = 5
print(obj)

# 使用单个值或序列，从DataFrame中索引一个或多个列
print("*" * 40)
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])

# 根据一个布尔值数组切片或选择数据
print("*" * 40)
print(data[:2])
print(data[data['three'] > 5])

# 使用布尔值DataFrame进行索引，布尔值DataFrame可以对标量值进行比较产生的
print("*" * 40)
print(data < 5)
data[data < 5] = 0
print(data)

# 5.2.3.1 使用loc和iloc选择数据
# 特殊索引符号loc和iloc
# 允许你使用轴标签(loc)或整数标签(iloc)以NumPy风格的语法从DataFrame中选出数组的行和列的子集
print("*" * 40)
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
print("*" * 40)
print(data.iloc[[1, 2], [3, 0, 1]])

# 索引用于切片
print("*" * 40)
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])
"""
DataFrame索引选项 df[val]: 从DataFrame中选择单列或列序列，特殊情况的遍历
布尔数组，切片或布尔值
"""

# 5.2.4 整数索引
print("*" * 40)
ser = pd.Series(np.arange(3.))
print(ser)
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2)
print(ser2[-1])

# 为了保持一致，如有一个包含整数的轴索引，数据选择时请始终使用标签索引
# 为了更精确地处理，可以使用loc（用于标签）或（用于整数）
print("*" * 40)
print(ser[:1])
print(ser.loc[:1])
print(ser.iloc[:1])

# 5.2.5 算术和数据对齐
# 如果存在某个索引对不相同，则返回结果的索引将是索引对的并集
print("*" * 40)
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1 + s2)

print("*" * 40)
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
# df1和df2相加，它的索引、列是每个DataFrame的索引、列的并集
print(df1 + df2)

# 如将两个行或列完全不同的DataFrame对象相加，结果将全部为空
print("*" * 40)
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)
print(df1 + df2)

# 5.2.5.1 使用填充值的算术方法
print("*" * 40)
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1)
print(df2)
print(df1 + df2)
# 在df1上使用add方法，将df2和一个fill_value作为参数传入
print(df1.add(df2, fill_value=0))

# 副本方法的参数是翻转的
print("*" * 40)
print(1 / df1)
print(df1.rdiv(1))

# 重建索引时，也可以指定不同的填充值
print("*" * 40)
print(df1.reindex(columns=df2.columns, fill_value=0))
"""
灵活算术方法
add,radd 加法
sub,rsub 减法
div,rdiv 除法
floordiv,rfloordiv 整除
mul,rmul 乘法
pow,rpow 幂次方
"""

# 5.2.5.2 DataFrame和Series间的操作
print("*" * 40)
# 运用到了广播机制
arr = np.arange(12.).reshape((3, 4))
pprint(arr)
pprint(arr[0])
pprint(arr - arr[0])

# DataFrame和Series之间操作是类似的
print("*" * 40)
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
pprint(frame)
pprint(series)

# 广播到行
print("*" * 40)
print(frame - series)

# 重建索引并形成联合
print("*" * 40)
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame +series2)

# 改为列上进行广播
print("*" * 40)
series3 = frame['d']
print(frame)
print(series3)
print(frame.sub(series3, axis='index'))

# 5.2.6 函数应用和映射
print("*" * 40)
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))

print("*" * 40)
f = lambda x: x.max() - x.min()
print(frame.apply(f))

print("*" * 40)
print(frame.apply(f, axis='columns'))

print("*" * 40)
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

print("*" * 40)
format = lambda x: '%.2f' % x
print(frame.applymap(format))

print("*" * 40)
print(frame['e'].map(format))

# 5.2.7 排序和排名
print("*" * 40)
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj)
print(obj.sort_index())

print("*" * 40)
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index())

print("*" * 40)
print(frame.sort_index(axis=1, ascending=False))

print("*" * 40)
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())

print("*" * 40)
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())

print("*" * 40)
print(frame.sort_values(by=['a', 'b']))

print("*" * 40)
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj)
print(obj.rank())
print(obj.rank(method='first'))

print("*" * 40)
print(obj.rank(ascending=False, method='max'))

print("*" * 40)
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis='columns'))

"""
排名中的平均关系打破方法
"""

"""
# 5.2.8 含有重复标签的轴索引
# 重复索引的Series
print("*" * 40)
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)

# is_unique属性，判断标签是否唯一
print(obj.index.is_unique)

# 重复索引：一个标签索引多个条目会返回一个序列，而单个条目会返回标量值
print("*" * 40)
print(obj['a'])
print(obj['c'])

# DataFrame中进行索引
print("*" * 40)
df  = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'])
"""
