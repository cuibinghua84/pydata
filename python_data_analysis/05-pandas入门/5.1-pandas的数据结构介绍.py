# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.1-pandas的数据结构介绍.py
@time: 2019/10/16 9:34
"""

from pprint import pprint
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 5.1.1 Series
print("Series是一种一维的数组型对象，它包含了一个值序列（与NumPy中的类型相似），并包含了数据标签，称为索引")
obj = pd.Series([4, 7, -5, 3])
# pprint(obj)
print(obj)

print("\n通过values和index属性分别获得Series对象的值和索引")
print(obj.values)
print(obj.index)

print("\n创建一个索引序列，用标签标识每个数据点")
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

print("\n标量、数学函数应用")
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# Series可以认为是一个长度固定且有序的字典
print('b' in obj2)
print('e' in obj2)

print("\n使用字典生成一个Series")
sdata = {'0hio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
# pprint(obj3)

print("\n可将字典键按照你想要的顺序传递给构造函数，从而使生成的Series的索引符合你的语气")
states = ['California', '0hio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

print("\npandas使用isnull和notnull函数来检查缺失数据")
print(pd.isnull(obj4))
print(pd.notnull(obj4))

print("\nisnull和notnull也是Series的实例方法")
print(obj4.isnull())

print("\n数学操作中自动对齐索引是Series的一个非常有用的特性")
print(obj3)
print(obj4)
print(obj3 + obj4)

print("\nSeries对象自身和其索引都有name属性，这个特性与pandas其他重要功能集在一起")
print(obj4)
print()
obj4.name = 'pupolation'
obj4.index.name = 'state'
print(obj4)

print("\nSeries的索引可以通过按位置赋值的方式进行行改变")
print(obj)
print()
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

# 5.1.2 DataFrame
# DataFrame表示的是矩阵的数据表，它包含已排序的列集合，每一列可以是不用的值类型
# DataFrame既有行索引也有列索引，它可以被视为一个共享相同索引的Series的字典
# 在DataFrame中，数据被存储为一个以上的二维块，而不是列表、字典或其他一维数组的集合
print("\nDataFrame")
data = {'state': ['0hio', '0hio', '0hio', 'Nevada', 'Nevada', 'Nevada'],
	   'year':[2000, 2001, 2002, 2001, 2002, 2003],
	   'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

print("\n对于大型DataFrame，head方法将会只选出头部的五行")
print(frame.head())

print("\n指定列的顺序，如果列不在字典中，将会出现缺失值")
# print(data)
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)

print("\n某一列，可以按字典标记或属性一样索引为Series")
print(frame2['state'])
print(frame2.year)
# 备注frame2[colunm]对于任意列名但是frame2.colunm只在列名是有效的Python变量名时有效

print("\n行也可以通过位置或特殊属性loc进行选取")
print(frame2.loc['three'])

print("\n列的引用是可以修改的")
frame2['debt'] = 16.5
print(frame2)
print()
frame2['debt'] = np.arange(6.)
print(frame2)

print("\n将Series赋值给一列时，Series的索引将会按照DataFrame的索引重新排列，并在空缺的地方填充缺失值")
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

print("\n如果被赋值的列并不存在，则会生产一个新的列")
frame2['eastern'] = frame2.state == '0hio'
print(frame2)

print("\ndel关键字可以像在字典中那样对DataFrame删除列；移除之前新建的列")
del frame2['eastern']
print(frame2.columns)

# 从DataFrame中选取的列是数据的视图，而不是拷贝。因此，对Series的修改会映射到DataFrame中
# 如需复制，则应当显式地使用Series的copy方法
print("\n包含字典的嵌套字典")
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, '0hio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
print("\n嵌套字典被赋值给DataFrame，pandas会将字典的键作为列，将内部字典的键作为行索引")
frame3 = pd.DataFrame(pop)
print(frame3)

print("\nDataFrame进行转置操作")
print(frame3.T)

print("\n如果已经显式地指明索引，内部字典的键将不会被排序")
print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

print("\n包含Series的字典也可以用于构造DataFrame")
pdata = {'0hio': frame3['0hio'][:-1], 'Nevada': frame3['Nevada'][:2]}
print(pd.DataFrame(pdata))

print("\nDataFrame的索引和列拥有name属性，name的属性也会被显示")
frame3.index.name = 'year'; 
frame3.columns.name = 'state'
print(frame3)

"""
DataFrame构造函数的有效输入
2D ndarray					数据的矩阵，行和列的标签是可选参数
数组、列表和元组构造的字典		每个序列成为DataFrame的一列，所有的序列必须长度相等
NumPy结构化/记录化数组		与数组构成的字典一致
Series构成的字典				每个值成为一列，每个Series的索引联合起来形成结果的行索引，也可以显式地传递索引
字典构成的字典				每一个内部字典成为一列，键联合起来形成结果的行索引
字典或Series构成的列表		列表中的一个元素形成DataFrame的一行，字典键或Series索引联合起来形成DataFrame的列标签
列表或元组构成的列表			与2Dndarray的情况一直
其他DataFrame				如果不显式地传递索引，则会使用原DataFrame的索引
NumPy MaskedArray			与2Dndarray的情况类型，但隐蔽值会在结果DataFrame中成为NA/缺失值
"""

# 5.1.3 索引对象
print("\n在构造Series和DataFrame时，使用的任意数组或标签序列都可以在内部转换为索引对象")
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])

print("\n索引对象是不可变的")
labels = pd.Index(np.arange(3))
print(labels)
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)

print("\n索引对象也像一个固定大小的集合")
print(frame3)
print(frame3.columns)
print('0hio' in frame3.columns)
print(2003 in frame3.index)

print("\npandas索引对象可以包含重复标签")
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)

"""
部分索引对象的方法和属性
append：			将额外的索引对象粘贴到原索引后，产生一个新的索引
difference：		计算两个索引的差集
intersection：	计算两个索引的交集
union：			计算两个索引的并集
isin： 			计算表示每一个值是否在传值容器中的布尔数组
delete： 		将位置i的元素删除，并产生新的索引
drop： 			根据传参删除指定索引值，并产生新的索引值
insert： 		在位置i插入元素，并产生行的索引
is_monotonic： 	如果索引序列递增则返回True
is_unique： 		如果索引序列唯一这返回True
unique： 		计算索引的唯一值序列
"""




