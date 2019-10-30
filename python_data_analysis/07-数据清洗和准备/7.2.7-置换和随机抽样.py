# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.2.7-置换和随机抽样.py
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

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
print(sampler)

print(df)
print(df.take(sampler))

print(df.sample(n=3))

choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
print(draws)