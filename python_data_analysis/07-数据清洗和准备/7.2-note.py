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

# 7.2.7 置换和随机抽样

# 7.2.8 计算指标/虚拟变量
