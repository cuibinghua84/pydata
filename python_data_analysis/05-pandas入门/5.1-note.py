# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.1-note.py
@time: 2019/11/13 9:20
"""

# 5.1 pandas数据结构介绍
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint

# 5.1.1 Series
# Series是一种一维的数组型对象，它包含了一个值序列，并且包含了数据标签，称为索引
obj= Series([4, 7, -5, 3])
# print(obj)

# values属性和index属性分别获得Series对象的值和索引
print(obj.values)
print(obj.index)

# 创建一个索引序列
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2)
# print(obj2.index)

# 使用标签来索引
print(obj2['a'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

# 操作
print(obj2)
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

print('b' in obj2)
print('e' in obj2)

# 使用字典生成一个Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
print(sdata)
obj3 = pd.Series(sdata)
print(obj3)

# 将字典键按照你想要的顺序传递
states = {'California', 'Ohio', 'Oregon', 'Texas'}
obj4 = pd.Series(sdata, index=states)
print(obj4)

# 检查缺失数据
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print(obj4.notnull())

# 数学操作中自动对齐
print(obj3)
print(obj4)
print(obj3 + obj4)

# Series对象自身和索引都有name属性
print("*" * 40)
print(obj4)
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# Series的索引通过按位置赋值的方式进行改变
print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

# 5.1.2 DataFrame
print("*" * 40)
# 构建DataFrame
# 利用包含等长度列表或NumPy数组的字典
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002, 2003], 
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

# head方法将会只选出头部五行
print("*" * 40)
print(frame.head())

# 指定列的顺序
print("*" * 40)
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

# 如果传入的列不在包含的字典中，将会出现缺失值
print("*" * 40)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'dept'], 
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)

# 按字典型标记或属性检索Series
print("*" * 40)
print(frame2['state'])
print(frame2.year)

# 行可以通过位置或特殊属性loc进行选取
print("*" * 40)
print(frame2.loc['three'])

# 修改列的引用
frame2['dept'] = 16.5
print(frame2)

frame2['dept'] = np.arange(6.)
print(frame2)

"""
当你将列表或数组赋值给一个列时，值的长度必须和DataFrame的长度相匹配。
如果你将Series赋值给一列时，Series的索引将会按照DataFrame的索引重新排列，
并在空缺的地方填充缺失值
"""
print("*" * 40)
val = pd.Series([2, -1.2, -1.5, -1.7], index=['one', 'two', 'four', 'five'])
frame2['dept'] = val
print(frame2)

# del
print("*" * 40)
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
del frame2['eastern']
print(frame2)
print(frame2.columns)
# 从DataFrame中选取的列是数据的视图，而不是拷贝

# 包含字典的嵌套：将内部字典的键作为行索引
print("*" * 40)
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)

# 使用NumPy语法对DataFrame机型转置
print(frame3.T)

print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

# Series字典构造DataFrame
print("*" * 40)
pdata = {'Ohio': frame3['Ohio'][:-1], 'Nevada': frame3['Nevada'][:2]}
# print(pdata)
print(pd.DataFrame(pdata))

print("如果DataFrame的索引和拥有name属性，则这些name属性也会被显示")
print("*" * 40)
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)

# DataFrame的values属性会将包含在DataFrame中的数据以二维ndarray的形式返回
print("*" * 40)
# pprint(frame3.values)

# 如果DataFrame的列是不同的dtypes，则values的dtype会自动选择适合所有列的类型
print("*" * 40)
print(frame2.values)
"""
DataFrame构造函数的有效输入
2D ndarray：
数组、列表和元组构成的字典：
NumPy结构化/记录化数组
Series构成的字典
字典构成的字典
字典或Series构成的列表
列表或元组构成的列表
其他DataFrame
NumPy MaskedArray
"""
print("*" * 40)

# 5.1.3 索引对象
# 任意数组或标签序列都也在内部转换为索引对象
obj = pd.Series(range(3), index=['a', 'b', 'c'])
print(obj)
index = obj.index
print(index)
print(index[1:])

# 索引对象是不可变的，不变性使得在多种数据结构中分享索引对象更为安全
print("*" * 40)
labels = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)

# 索引对象也是一个固定大小的集合
print("*" * 40)
print(frame3)
print(frame3.columns)
print('Ohio' in frame3.columns)
print(2003 in frame3.index)

# pandas索引对象可以包含重复标签
print("*" * 40)
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)
"""
一些索引对象的方法和属性
append 将额外的索引对象黏贴到原索引后，产生一个新的索引
difference 计算两个索引的差集
intersection 计算两个索引的交集
union 计算两个索引的并集
isin 计算表示每一个值是否在传值容器中的布尔数组
delete 将位置i的元素删除，并产生新的索引
drop 根据传参删除指定的索引值，并产生新的索引
insert 在位置i插入元素，并产生新的索引
is_monotonic 如果索引序列递增则返回True
is_unique 如果索引序列唯一则返回True
unique 计算索引的唯一序列
"""



