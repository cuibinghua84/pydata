# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/19 14:03
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from numpy import nan as NA
from pprint import pprint
import re

def fs():
    print("*" * 50)


# 7.1 处理缺失值
string_data = Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())

fs()
string_data[0] = None
print(string_data)
print(string_data.isnull())
"""
NA处理方法
dropna
fillna
isnull
notnull
"""

# 7.1.1 过滤缺失值
fs()
data = Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print(data[data.notnull()])

fs()
data = DataFrame([[1., 6.5, 3.], [1., NA, NA],
                  [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
print(data)
print(cleaned)

fs()
print(data.dropna(how='all'))

fs()
data[4] = NA
print(data)
print(data.dropna(axis=1, how='all'))

fs()
df = DataFrame(np.random.randn(7, 3))
print(df)
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())

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
df = DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))

fs()
data = Series([1, NA, 3.5, NA, 7])
print(data)
print(data.fillna(data.mean()))
"""
fillna函数参数
value
method
axis
inplace
limit
"""

# 7.2 数据转换
# 7.2.1 删除重复值
fs()
data = DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())

fs()
data['v1'] = range(7)
print(data)
fs()
print(data.drop_duplicates(['k1']))

fs()
print(data.drop_duplicates(['k1', 'k2'], keep='last'))

# 7.2.2 使用函数或映射进行数据转换
fs()
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                           'Pastrami', 'corned beef', 'Bacon',
                           'pastrami', 'honey ham', 'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

fs()
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
print(lowercased)

fs()
data['animal'] = lowercased.map(meat_to_animal)
print(data)

fs()
print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

# 7.2.3 替代值
fs()
data = Series([1., -999., 2., -999., -1000., 3.])
print(data)
print(data.replace(-999, np.nan))
print(data.replace([-999, -1000], np.nan))

fs()
print(data.replace([-999, -1000], [np.nan, 0]))

fs()
print(data.replace({-999: np.nan, -1000: 0}))

# 7.2.4 重命名轴索引
fs()
data = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data)
transform = lambda x: x[:4].upper()
# print(transform)
print(data.index.map(transform))

data.index = data.index.map(transform)
print(data)

fs()
print(data.rename(index=str.title, columns=str.upper))

fs()
print(data.rename(index={'OHIO': 'INDIANA'},
                  columns={'three': 'peekaboo'}))

fs()
data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
print(data)

# 7.2.5 离散化和分箱
fs()
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
# print(cats)
# pprint(cats.codes)
# pprint(cats.categories)
print(pd.value_counts(cats))

fs()
print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

fs()
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

fs()
data = np.random.rand(20)
# print(data)
print(pd.cut(data, 4, precision=2))

fs()
data = np.random.randn(1000)
cats = pd.qcut(data, 4)
# print(cats)
print(pd.value_counts(cats))

fs()
print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))

# 7.2.6 检测和过滤异常值
fs()
data = DataFrame(np.random.randn(1000, 4))
# print(data)
print(data.describe())

fs()
col = data[2]
print(col[np.abs(col) > 3])
print(data[(np.abs(data) > 3).any(1)])

fs()
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())

fs()
print(np.sign(data).head())

# 7.2.7 置换和随机抽样
fs()
df = DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
pprint(sampler)

fs()
print(df)
fs()
print(df.take(sampler))

fs()
print(df.sample(n=3))

fs()
choices = Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
print(draws)

# 7.2.8 计算指标/虚拟变量
fs()
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})
print(df)
print(pd.get_dummies(df['key']))

fs()
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

fs()
'''
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table("D:/data/pydata_book2/datasets/movielens/movies.dat", sep='::',
              header=None, names=mnames, engine='python')
# print(movies[:10])

all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
print(genres)
zero_marix = np.zeros((len(movies), len(genres)))
dummies = DataFrame(zero_marix, columns=genres)
gen = movies.genres[0]
print(gen.split("|"))
pprint(dummies.columns.get_indexer(gen.split('|')))
'''

# 7.3 字符串操作
# 7.3.1 字符串对象方法
val = 'a, b,  guido'
print(val.split(','))
pieces = [x.strip() for x in val.split(', ')]
print(pieces)

first, second, third = pieces
print(first + '::' + second + '::' + third)
print('::'.join(pieces))
print('guido' in val)
print(val.index(','))
print(val.find(':'))
print(val.count(','))
print(val.replace(',', '::'))
print(val.replace(',', ''))
'''
Python内建字符串方法
val.count()
val.endswith()
val.startswith()
val.join()
val.index()
val.find()
val.rfind()
val.replace()
val.strip()
val.rstrip()
val.lstrip()
val.split()
val.lower()
val.upper()
val.casefold()
val.ljust()
val.rjust()
'''

# 7.3.2 正则表达式
# 需要的时候专享学习
"""
正则表达式方法
findall
finditer
match
search
split
sub，subn
"""

# 7.3.3 pandas中向量化字符串函数
fs()
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = Series(data)
print(data)
print(data.isnull())

fs()
print(data.str.contains('gmail'))
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
print(pattern)
print(data.str.findall(pattern, flags=re.IGNORECASE))

fs()
matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)

fs()
# print(matches.str.get(1))
# print(matches.str[0])
# print(data.str[:5])


