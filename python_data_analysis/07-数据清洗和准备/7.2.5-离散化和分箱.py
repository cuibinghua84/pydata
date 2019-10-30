# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.2.5-离散化和分箱.py
@time: 2019/10/30 9:53
"""

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint
import sys
import csv
import json

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)

print(cats.codes)
print(cats.categories)
print(pd.value_counts(cats))

print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))

print()
data = np.random.randn(1000)
cats = pd.qcut(data, 4)
print(cats)
print(pd.value_counts(cats))

print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))
