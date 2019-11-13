# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.3-note.py
@time: 2019/11/13 9:20
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web

# 5.3 描述性统计的概述与计算
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], 
                  index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df)

# sum():列上加和；axis='columns'或axis=1 则会将一行上各个列的值相加
print("*" * 40)
print(df.sum())

print(df.sum(axis='columns'))

# 通过skipna实现不排斥NA值
print(df.mean(axis='columns', skipna=False))
"""
归纳方法可选参数
axis：归约轴，0为行向 1为列向
skipna 排除缺失值 默认为True
level 如果轴是多层索引的，该参数可以缩减分组层级
"""

print("*" * 40)
# idxmin idxmax
print(df.idxmax())
print(df.idxmin())
print(df.cumsum())

# 一次性产生多个汇总统计：describe
print("*" * 40)
print(df.describe())

# 非数值型数据，describe的汇总统计
print("*" * 40)
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())

"""
描述性统计和汇总统计
count 非NA值的个数
describe 计算Series或DataFrame各列汇总统计集合
min，max 计算最小值 最大值
argmin argmax 分别计算最小值 最大值所在的索引位置(整数)
idxmin idxmax 分别计算最小值 最大值所在的索引标签
quantile 计算样本的从0到1间的分位数
sum 加和
mean 均值
median 中位数
mad 平均值的平均绝对偏差
prod 所有值的积
var 值的样本方差
std 值的样本标准差
skew 样本偏度值
kurt 样本峰度的值
cumsum 累积值
cummin cummax 累积值的最小值 最大值
cumprod 值的累计积
diff 计算第一个算术差值（对时间序列有用）
pct_change 计算百分比
"""

# 5.3.1 相关性和协方差
"""
print("*" * 40)
# 股价的百分比 时间序列操作
all_data = {ticker: web.get_data_yahoo(ticker) for ticker in['AAPL', 'IBM', 'MSFT', 'GOOG']}
price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
returns = price.pct_change()
print(returns.tail())
print(returns['MSFT'].corr(returns['IBM']))
print(returns['MSFT'].cov(returns['IBM']))
print(returns.MSFT.corr(returns.IBM))

print("*" * 40)
# corr cov返回相关性和协方差矩阵
print(returns.corr())
print(returns.cov())

# corrwith计算相关性
print("*" * 40)
print(returns.corrwith(returns.IBM))

# 计算交易量百分比变化的相关性
print("*" * 40)
print(returns.corrwith(volume))
"""

# 5.3.2 唯一值、计数和成员属性
print("*" * 40)
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
# unique
uniques = obj.unique()
print(uniques)
print(obj.value_counts())
print(pd.value_counts(obj.values, sort=False))

# isin执行向量化的成员属性检查
print("*" * 40)
print(obj)
mask = obj.isin(['b', 'c'])
print(mask)
print(obj[mask])

# index.get_indexer
print("*" * 40)
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
print(pd.Index(unique_vals).get_indexer(to_match))

"""
唯一值、计数和集合成员属性方法
isin 计算表征Series中每个值是否包含于传入序列的布尔值数组
match 计算数组中每个值的整数索引，形成一个唯一值数组，有助于数据对齐和join类型的操作
unique 计算Series值中的唯一值数组，按照观察顺序返回
value_counts 返回一个Series，索引是唯一值序列，值是计数个数，按照个数降序排序
"""
print("*" * 40)
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3],
                     'Qu3': [1, 5, 2, 4, 4]})
print(data)
result = data.apply(pd.value_counts).fillna(0)
print(result)


