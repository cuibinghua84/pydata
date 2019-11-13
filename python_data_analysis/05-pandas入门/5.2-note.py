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

# 5.2.2 轴向上删除条目

# 5.2.3 索引、选择与过滤

# 5.2.3.1 使用loc和iloc选择数据

# 5.2.4 整数索引

# 5.2.5 算术和数据对齐

# 5.2.5.1 使用填充值的算术方法

# 5.2.5.2 DataFrame和Series间的操作

# 5.2.6 函数应用和映射

# 5.2.7 排序和排名

# 5.2.8 含有重复标签的轴索引

