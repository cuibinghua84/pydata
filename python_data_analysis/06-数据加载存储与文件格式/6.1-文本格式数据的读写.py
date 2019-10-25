# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.1-文本格式数据的读写.py
@time: 2019/10/22 11:23
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint



"""输入和输出通常有以下几种类型：
读取文本文件及硬盘上其他更高效的格式文件
从数据库载入数据
与网络资源进行交互(比如WebAPI)"""

# 6.1 文本格式数据的读写
"""将表格型数据读取为DataFrame对象是pandas的重要特性
Pandas的解析函数
read_csv		从文件、URL或文件型对象读取分隔好的数据，逗号是默认分隔符
read_table 		从文件、URL或文件型对象读取分隔好的数据，制表符('\t')是默认分隔符
read_fwf		从特定宽度格式的文件中读取数据(五分隔符)
read_clipboard	read_table的剪切板版本，在将表格从Web页面上转换成数据时有用
read_excel		从Excel的XLS或XLSX文件中读取表格数据
read_hdf		读取pandas纯纯的HDF5文件
read_html		从HTML文件中读取所有表格数据
read_json		从JSON字符串中读取数据
read_msgpack	读取MessagePack二进制格式的pandas数据
read_pickle		读取以Python pickle格式存储的任意对象
read_sas		读取存储在SAS系统中定制存储格式的SAS数据集
read_sql		将SQL查询的结果，读取为pandas的DataFrame
read_stata		读取Stata格式的数据集
read_feather	读取Feather二进制格式

以上函数的可选参数
索引： 可以将一活多个列作为返回的DataFrame，从文件或用户处获得列名，或者没有列名
类型推断和数据转换：包括用户自定义的值转换和自定义的缺失值符号列表
日期时间解析：包括组合功能，也包括将分散在多个列上的日期和时间信息组合成结果中的单个列
迭代：支持对大型文件的分块迭代
未清洗数据问题：跳过行、页脚、注释以及其他次要数据"""

print("read_csv读取逗号分隔的文件")
path_1 = "D:/data/pydata_book2/examples/ex2.csv"

print("\n默认列名")
df = pd.read_csv(path_1, header=None)
print(df)

print("\n指定列名")# 
df = pd.read_csv(path_1, names=['a', 'b', 'c', 'd', 'message'])
print(df)

print("\n将message列称为DataFrame的索引，指定位置4的列为索引，或将'message'传递给参数index_col")
names = ['a', 'b', 'c', 'd', 'message']
print(pd.read_csv(path_1, names = names, index_col='message'))

print("\n从多列中形成分层索引，需传入一个包含序列号或列名的表")
path_2 = "D:/data/pydata_book2/examples/csv_mindex.csv"
parsed = pd.read_csv(path_2, index_col=['key1', 'key2'])
print(parsed)


# 6.1.1 分块读入文本文件


# 6.1.2 将数据写入文本文件

# 6.1.3 使用分隔格式

# 6.1.4 JSON数据

# 6.1.5 XML和HTML：网络抓取

# 6.1.5.1 使用lxml.objectify解析XML


