# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:58:35 2019

@author: p_bhcui
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy import nan as NA

def fs():
    print("*" * 40)

# 7.1 处理缺失值
# 7.1.1 过滤缺失值
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())

fs()
string_data[0] = None
print(string_data)
print(string_data.isnull())
"""
NA处理方法
dropna 根据每个标签的值是否是缺失数据来筛选轴标签，并根据允许丢失的数据来确定阀值
fillna 用某些值填充缺失的数据或使用插值方法：ffill bfill
isnull 返回表明哪些值是缺失值的布尔值
notnull isnull的反函数
"""

fs()
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())

fs()
print(data[data.notnull()])

fs()
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
print(data)

fs()
print(cleaned)

fs()
print(data.dropna(how='all'))

fs()
data[4] = NA
print(data)
print(data.dropna(axis=1, how='all'))

fs()
df = pd.DataFrame(np.random.randn(7, 3))
print(df)
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)

fs()
print(df.dropna())
print(df.dropna(thresh=2))

# 7.1.2 补全缺失值
fs()
print(df)
print(df.fillna(0))

fs()
print(df.fillna({1: 0.5, 2: 0}))

fs()
_ = df.fillna(0, inplace=True)
print(df)

fs()
df = pd.DataFrame(np.random.randn(6, 3))
print(df)
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
fs()
print(df.fillna(method='ffill'))

fs()
print(df.fillna(method='ffill', limit=2))

fs()
data = pd.Series([1., NA, 3.5, NA, 7])
print(data)
print(data.fillna(data.mean()))
"""
fillna函数参数
value 标量值或字典型对象用于填充缺失值
method 插值方法，如果没有其他参数，默认是'ffill'
axis 需要填充的轴，默认axis=0
inplace 修改被调用的对象，而不是生成一个备份
limit 用于向前或向后填充时最大的填充范围
"""

