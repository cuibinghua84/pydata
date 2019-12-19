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
print(data['b'])
print(data['b': 'c'])
print(data.loc[['b', 'd']])
print(data.loc[:, 2])


# 8.2 联合与合并数据集

# 8.3 重塑与透视



