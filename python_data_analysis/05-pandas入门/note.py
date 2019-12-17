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


# 5.2 基本功能

# 5.3 描述性统计的概述与计算
