# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:52:07 2019

@author: p_bhcui
"""

import numpy as np
import pandas as pd
from pandas import DataFrame, Series

def fs():
    print("*" * 40)

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': np.random.randn(5),
                   'data2': np.random.randn(5)})
print(df)

grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())

means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means)

print(means.unstack())

fs()
states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states, years]).mean())

fs()
print(df.groupby('key1').mean())
print(df.groupby(['key1', 'key2']).mean())

fs()
print(df.groupby(['key1', 'key2']).size())

fs()
for name, group in df.groupby('key1'):
    print(name)
    print(group)

fs()
for (k1, k2), group in df.groupby(['key1', 'key2']):
    print((k1, k2))
    print(group)