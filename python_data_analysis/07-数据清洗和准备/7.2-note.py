# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:59:04 2019

@author: p_bhcui
"""
import numpy as np
import pandas as pd
from pprint import pprint


def fs():
    print("*" * 40)


# 数据转换
# 7.2.1 删除重复值
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

print(data.duplicated())
print(data.drop_duplicates())

fs()
data['v1'] = range(7)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k1', 'k2'], keep='last'))

# 7.2.2 使用函数或映射进行数据转换
fs()
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                              'corned beef', 'Bacon', 'pastrami', 'honey ham',
                              'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

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
data['animal'] = lowercased.map(meat_to_animal)
print(data)
print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

# 7.2.3 替代值
fs()
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
print(data.replace(-999, np.nan))

fs()
print(data.replace([-999, -1000], np.nan))
fs()
print(data.replace([-999, -1000], [np.nan, 0]))
fs()
print(data.replace({-999: np.nan, -1000: 0}))

# 7.2.4 重命名轴索引
fs()
data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

transform = lambda x: x[:4].upper()
print(data.index.map(transform))

fs()
data.index = data.index.map(transform)
print(data)

fs()
print(data.rename(index=str.title, columns=str.upper))

print(data.rename(index={'OHIO': 'INDIANA'}, columns={'three': 'peekaboo'}))

data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
print(data)

# 7.2.5 离散化和分箱
fs()
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
pprint(cats)
pprint(cats.codes)
pprint(cats.categories)
pprint(pd.value_counts(cats))

fs()
print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

fs()
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

fs()
data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))

fs()
data = np.random.rand(1000)
cats = pd.qcut(data, 4)
pprint(cats)

fs()
print(pd.value_counts(cats))

fs()
print(pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.]))

# 7.2.6 检测和过滤异常值
fs()
data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[2]
print(col[np.abs(col) > 3])

fs()
print(data[(np.abs(data) > 3).any(1)])

fs()
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())

fs()
print(np.sign(data).head())

# 7.2.7 置换和随机抽样
fs()
df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
pprint(df)
sampler = np.random.permutation(5)
pprint(sampler)

fs()
print(df)
print(df.take(sampler))

fs()
print(df.sample(n=3))

fs()
choices = pd.Series([5, 7, -1, 6, 4])
pprint(choices)
draws = choices.sample(n=10, replace=True)
pprint(draws)

# 7.2.8 计算指标/虚拟变量
fs()
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'], 'data1': range(6)})
print(pd.get_dummies(df['key']))

fs()
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

fs()
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('D:/data/pydata_book2/datasets/movielens/movies.dat', sep='::',
                       header=None, names=mnames, engine='python')
pprint(movies[:10])

fs()
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
pprint(genres)

fs()
zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)
gen = movies.genres[0]
print(gen.split('|'))
print(dummies.columns.get_indexer(gen.split('|')))

fs()
for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.iloc[0])

fs()
np.random.seed(12345)
values = np.random.rand(10)
print(values)

fs()
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
print(pd.get_dummies(pd.cut(values, bins)))
