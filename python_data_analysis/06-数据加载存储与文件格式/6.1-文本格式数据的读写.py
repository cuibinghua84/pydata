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

print("\n不固定的分隔符，如空白或其他，可以向read_table传递一个正则表达式作为分隔符")
pprint(list(open("D:/data/pydata_book2/examples/ex3.txt")))

print("\n正则表达式为\s+")
result = pd.read_table('D:/data/pydata_book2/examples/ex3.txt', sep='\s+')
pprint(result)

print("\n使用skiprows跳过第一行、第三行和第四行")
pprint(list(open("D:/data/pydata_book2/examples/ex4.csv")))
pprint(pd.read_csv('D:/data/pydata_book2/examples/ex4.csv', skiprows=[0, 2, 3]))

print("\n缺失值处理")
result = pd.read_csv("D:/data/pydata_book2/examples/ex5.csv")
pprint(result)
pprint(pd.isnull(result))

print("\nna_values选项可以传入一个列表或一组字符串来处理缺失值")
result = pd.read_csv("D:/data/pydata_book2/examples/ex5.csv", na_values=['NULL'])
pprint(result)

print("\n指定不同的缺失值标识")
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pprint(pd.read_csv('D:/data/pydata_book2/examples/ex5.csv', na_values=sentinels))

"""read_csv/read_table函数参数
path 				表明文件系统位置的字符串，URL或文件型对象
sep或delimiter 		用于分隔每行字段的字符序列或正则表达式
header 				用作列名的行号，默认是0（第一行）如果没有列名的话，应该为None
index_col 			用作结束中行索引的列号或列名，可以是一个单一的名称/数字，也可以是一个分层索引
names 				结果的列名列表，和header=None一起用
skiprows 			从文件头处起，需要跳过的行数或行号列表
na_values           需要用NA替换是值序列
comment 			在行结尾处分隔注释的字符
parse_dates 		尝试将数据解析为datetime，默认是False。如果为True，将尝试解析所有的列，也可以指定行号或列名来进行解析
					，如果列表的元素是元组或列表，将会把多个列组合在一起进行解析（例如日期/时间将拆分为两列）
keep_data_col 		如果连接类到解析日期上，保留被连接的列，默认是False
converters 			包含列名称映射到函数的字典（例如{'foo': f}会把函数f应用到'foo'列）
dayfirst 			解析非明确日期时，按照国际格式处理(例如 7/6/2012->June,7,2012)，默认为False"""




# 6.1.1 分块读入文本文件


# 6.1.2 将数据写入文本文件

# 6.1.3 使用分隔格式

# 6.1.4 JSON数据

# 6.1.5 XML和HTML：网络抓取

# 6.1.5.1 使用lxml.objectify解析XML