# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/17 16:31
"""

from pprint import pprint
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import  pandas_datareader.data as web

def fs():
    print("*" * 50)


# 5.1 pandas数据结构介绍
# 5.1.1 Series
obj = pd.Series([4, 7, -5, 3])
pprint(obj)
pprint(obj.values)
pprint(obj.index)

fs()
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
pprint(obj2)

fs()
print(obj2['a'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

fs()
pprint(obj2)
print(obj2[obj2 > 0])
# exp() 方法返回x的指数,ex
print(obj2 * 2)
print(np.exp(obj2))

fs()
print('b' in obj2)
print('e' in obj2)

fs()
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

fs()
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

fs()
print(pd.isnull(obj4))
print(pd.notnull(obj4))

fs()
print(obj4.isnull())
print(obj4.notnull())

fs()
print(obj3)
print(obj4)
print(obj3 + obj4)

fs()
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

fs()
print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

# 5.1.2 DataFrame
fs()
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head())

fs()
print()
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)

fs()
print(frame2['state'])
print(frame2.year)

fs()
print(frame2.loc['three'])

fs()
print(frame2)
frame2['debt'] = 16.5
print(frame2)

fs()
frame2['debt'] = np.arange(6.)
print(frame2)

fs()
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

fs()
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
del frame2['eastern']
print(frame2.columns)
print(frame2)

fs()
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6},
       'Hua': {2019: 6.6, 2020: 8.8}}
frame3 = pd.DataFrame(pop)
print(frame3)

fs()
print(frame3.T)

fs()
print(pd.DataFrame(pop, index=[2001, 2002, 2003, 2019, 2020]))

fs()
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

fs()
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)

fs()
pprint(frame3.values)
pprint(frame2.values)
"""
DataFrame构造函数的有效输入
"""

# 5.1.3 索引对象
fs()
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])

fs()
labels = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)

fs()
print(frame3)
print(frame2.columns)
print('Ohio' in frame3.columns)
print(2003 in frame3.index)

fs()
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)
"""
索引对象的方法和属性
append
difference
intersection
union
isin
delete
drop
insert
is_monotonic
is_unique
unique
"""

# 5.2 基本功能
# 5.2.1 重建索引
fs()
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

fs()
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
print(obj3.reindex(range(6), method='ffill'))

fs()
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
pprint(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

fs()
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))

fs()
# print(frame.loc[['a', 'b', 'c', 'd'], states])
# 5.2.2 轴向上删除条目
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
# print(obj)
print(obj.drop(['d', 'c']))

fs()
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utha', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

fs()
print(data.drop(['Colorado', 'Ohio']))

fs()
print(data.drop('two', axis=1))

fs()
print(data.drop(['two', 'four'], axis='columns'))

fs()
print(obj)
obj.drop('c', inplace=True)
print(obj)

# 5.2.3 索引、选择与过滤
fs()
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

fs()
print(obj['b': 'c'])

obj['b': 'c'] = 5
print(obj)

fs()
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New Your'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

fs()
print(data['two'])

fs()
print(data[['three', 'one']])

fs()
print(data[:2])
print(data[data['three'] > 5])

fs()
print(data < 5)

fs()
data[data < 5] = 0
print(data)

# 5.2.3.1 使用loc和iloc选择数据
fs()
print(data)
print(data.loc['Colorado', ['two', 'three']])

fs()
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])

fs()
print(data)
print(data.iloc[[1, 2], [3, 0, 1]])

fs()
print(data)
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])

# 5.2.4 整数索引
fs()
ser = pd.Series(np.arange(3.))
print(ser)
# print(ser[-1])
print(ser[:1])
print(ser.loc[:1])
print(ser.iloc[:1])

fs()
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2)
print(ser2[-1])

# 5.2.5 算术和数据对齐
fs()
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1 + s2)

fs()
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                   index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1)
print(df2)
print(df1 + df2)

fs()
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)
print(df1 + df2)
print(df1 - df2)

# 5.2.5.1 使用填充值的算术方法
fs()
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
print(df1)
print(df2)

fs()
df2.loc[1, 'b'] = np.nan
print(df1)
print(df2)

fs()
print(df1 + df2)
fs()
print(df1.add(df2, fill_value=0))

fs()
print(1 / df1)
print(df1.rdiv(1))

fs()
print(df1.reindex(columns=df2.columns, fill_value=0))
"""
灵活算术方法
add radd
sub rsub
div rdiv
floordiv rfloordiv
mul rmul
pow rpow
"""

# 5.2.5.2 DataFrame和Series间的操作
fs()
arr = np.arange(12.).reshape((3, 4))
pprint(arr)
pprint(arr[0])
print(arr - arr[0])

fs()
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame)
print(series)

fs()
print(frame - series)

fs()
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(series2)
print(frame)
print(frame + series2)

fs()
series3 = frame['d']
print(frame)
print(series3)

fs()
print(frame.sub(series3, axis='index'))

# 5.2.6 函数应用和映射
fs()
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))

fs()
f = lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.apply(f, axis='columns'))

fs()
def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

fs()
format = lambda x: '%.2f' % x
print(frame.applymap(format))

fs()
print(frame['e'].map(format))

# 5.2.7 排序和排名
fs()
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())

fs()
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))
print(frame.sort_index(axis=1, ascending=False))

fs()
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())

fs()
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())

fs()
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))

fs()
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj)
print(obj.rank())

fs()
print(obj.rank(method='first'))

fs()
print(obj.rank(ascending=False, method='max'))
"""
排名中的平级关系打破方法
average
min
max
first
dense
"""
fs()
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1],
                      'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis='columns'))

# 5.2.8 含有重复标签的轴索引
fs()
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
print(obj.index.is_unique)
print(obj['a'])
print(obj['c'])

fs()
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'])

# 5.3 描述性统计的概述与计算
fs()
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)

fs()
print(df.sum())

fs()
print(df.sum(axis='columns'))

fs()
print(df.mean(axis='columns', skipna=False))
"""
规约方法可选参数
axis
skipna
level
"""
fs()
print(df.idxmax())
print(df.cumsum())
print(df.describe())

fs()
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())
"""
描述性统计和汇总统计
count
describe
min max
argmin argmax
idxmin idxmax
quantitle
sum
mean
median
mad
prod
var
std
skew
kurt
cumsum
cummin cummax
cumprod
diff
pct_change
"""

# 5.3.1 相关性和协方差
fs()
"""
all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

returns = price.pct_change()
pprint(returns.tail())

fs()
print(returns['MSFT'].corr(returns['IBM']))
print(returns['MSFT'].cov(returns['IBM']))

fs()
print(returns.MSFT.corr(returns.IBM))

fs()
print(returns.corr())

fs()
print(returns.cov())

fs()
print(returns.corrwith(returns.IBM))

fs()
print(returns.corrwith(volume))
"""
# 5.3.2 唯一值、计数和成员属性
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
pprint(uniques)

fs()
print(obj.value_counts())

fs()
print(pd.value_counts(obj.values, sort=False))

fs()
print(obj)
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

fs()
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
pprint(pd.Index(unique_vals).get_indexer(to_match))

fs()
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4],
                     'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
result = data.apply(pd.value_counts).fillna(0)
print(result)


