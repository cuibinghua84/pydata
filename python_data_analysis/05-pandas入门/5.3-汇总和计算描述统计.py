# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.3-汇总和计算描述统计.py
@time: 2019/10/16 9:34
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 5.3.1 相关性和协方差
print("")
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df)
print(df.sum())

print("\n")
print(df.sum(axis='columns'))

print("\n")
print(df.mean(axis='columns', skipna=False))
"""
归纳方法可选参数
axis： 		约简的轴。DataFrame的行用0，列用1
skipna：		排除缺失值，默认值为True
level：		如何轴是层次化索引的，则根据level汉族约检
"""

print("\n")
print(df)
print(df.idxmax())
print(df.cumsum())

print("\n")
print(df.describe())

print("\n")
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())

"""
count			非NA值的个数
describe 		计算Series或DataFrame各列的汇总统计集合
min,max 		计算最小值 最大值
argmin, argmax 	分别计算最小值 最大值所在的索引位置(整数)
idxmin, idxmax 	分别计算最小值或最大值所在的索引标签
quantile 		计算样本的从0到1间的分位数
sum 			加和
mean 			均值
median			中位数
mad 			平均值的平均绝对偏差
prod 			所有值的积
var 			值的样本方差
std 			值的样本标准差
skew 			样本偏度值（第三时刻）
kurt 			样本偏度值（第四时刻）
cumsum 			累积值
cummin, cummax 	累积值的最小值或最大值
cumprod 		值的累积值
diff 			计算第一个算术差值（对时间序列有用）
pct_change 		计算百分比
"""

# 5.3.2 唯一值、计数和成员属性
# print("\n")

# print("\n")

# print("\n")

# print("\n")

# print("\n")

# print("\n")

# print("\n")
