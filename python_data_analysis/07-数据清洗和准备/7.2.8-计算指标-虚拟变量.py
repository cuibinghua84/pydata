# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.2.8-计算指标-虚拟变量.py
@time: 2019/10/30 9:58
"""

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint
import sys
import csv
import json

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

print("*" * 50)
mnames = ['movid_id', 'title', 'genres']
movies = pd.read_csv('D:/data/pydata_book2/datasets/movielens/movies.dat', sep='::', header=None, names=mnames, engine='python')
pprint(movies[:10])
print("*" * 50)
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
pprint(genres)

print("*" * 70)
zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)
gen = movies.genres[0]
pprint(gen.split('|'))
pprint(dummies.columns.get_indexer(gen.split('|')))