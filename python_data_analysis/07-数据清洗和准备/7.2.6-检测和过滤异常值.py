# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.2.6-检测和过滤异常值.py
@time: 2019/10/30 9:54
"""

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint
import sys
import csv
import json

data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[2]
print(col[np.abs(col) > 3])

print(data[(np.abs(data) > 3).any(1)])

data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())

print(np.sign(data).head())