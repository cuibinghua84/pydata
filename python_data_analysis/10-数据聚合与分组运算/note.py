# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/20 9:50
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import nan as NA
from pprint import pprint


def fs():
    print("*" * 50)


# 10.1 GroupBy机制
df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                'key2': ['one', 'two', 'one', 'two', 'one'],
                # 'data1': np.random.randn(5),
                'data1': [1, 2, 3, 4, 5],
                # 'data2': np.random.randn(5),
                'data2': [6, 7, 8, 9, 10]})

print(df)

fs()
grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())

fs()
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means)

# 10.1.1 遍历各分组

# 10.1.2 选择一列或所有列的子集

# 10.1.3 使用字典或Series分组

# 10.1.4 使用函数分组

# 10.1.5 根据索引层级分组

# 10.2 数据聚合

# 10.3 应用：通用拆分-应用-联合

# 10.4 数据透视表与交叉表
