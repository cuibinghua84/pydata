# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:26:09 2019

@author: p_bhcui
"""

import numpy as np
import pandas as pd
from pprint import pprint
import sys
import csv
import json

# 6.1 文本格式数据的读取

def fs():
    print("*" * 40)

"""
pandas的解析函数
pd.read_csv       
pd.read_table
pd.read_fwf
pd.read_clipboard
pd.read_excel
pd.read_hdf
pd.read_html
pd.read_json
pd.read_msgpack
pd.read_pickle
pd.read_sas
pd.read_sql
pd.read_stata
pd.read_feather

以上函数的可选参数的类型
1 索引
2 类型推断和数据转换
3 日期时间解析
4 迭代
5 未清洗数据问题
"""

# 逗号分隔文本文件
# read_csv
df = pd.read_csv('D:/data/pydata_book2/examples/ex1.csv')
print(df)

# read_table
fs()
print(pd.read_table("D:/data/pydata_book2/examples/ex1.csv", sep=','))

# 不包含表头行，pd可自动分配默认列名，也可以指定列名
# 默认列名
fs()
print(pd.read_csv("D:/data/pydata_book2/examples/ex2.csv", header=None))
# 指定列名
fs()
print(pd.read_csv("D:/data/pydata_book2/examples/ex2.csv", names=['a', 'b', 'c', 'd', 'message']))

# 指定message为索引
fs()
names = ['a', 'b', 'c', 'd', 'message']
print(pd.read_csv("D:/data/pydata_book2/examples/ex2.csv", names=names, index_col='message'))

# 从多个列中形成一个分层索引，需要传递一个包含序列号或列明的列表
fs()
parsed = pd.read_csv('D:/data/pydata_book2/examples/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

fs()
pprint(list(open('D:/data/pydata_book2/examples/ex3.txt')))
result = pd.read_table('examples/ex3.txt', sep='\s+')
pprint(result)

fs()
pprint(pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3]))

fs()
result = pd.read_csv('examples/ex5.csv')
pprint(result)
pprint(pd.isnull(result))

fs()
result = pd.read_csv('examples/ex5.csv', na_values=['NULL'])
pprint(result)
sentinles = {'message': ['foo', 'NA'], 'something': ['two']}
pprint(pd.read_csv('examples/ex5.csv', na_values=sentinles))
"""
read_csv/read_table函数参数
path
sep delimiter
header
index_col
names
skiprows
na_values
comment
parse_dates
keep_data_col
converters
dayfirst
"""

# 6.1.1 分块读入文本文件
fs()
pd.options.display.max_rows = 10
result = pd.read_csv('examples/ex6.csv')
# pprint(result)
pprint(pd.read_csv('examples/ex6.csv', nrows=5))

fs()
chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
pprint(chunker)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
    tot = tot.sort_values(ascending=False)
pprint(tot[:10])

# 6.1.2 将数据写入文本格式
fs()
data = pd.read_csv('examples/ex5.csv')
pprint(data)
pprint(data.to_csv('examples/out.csv'))

fs()
pprint(data.to_csv(sys.stdout, sep='|'))

fs()
pprint(data.to_csv(sys.stdout, na_rep='NULL'))

fs()
pprint(data.to_csv(sys.stdout, index=False, header=False))

fs()
pprint(data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c']))

fs()
dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
print(ts)
# ts.to_csv('examples/tseries.csv')

# 6.1.3 使用分割格式
fs()
f = open('examples/ex7.csv')
reader = csv.reader(f)
print(reader)
for line in reader:
    print(line)
fs()
with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
pprint(data_dict)

fs()
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = '; '
    quotecher = '"'
    quoting = csv.QUOTE_MINIMAL
# reader = csv.reader(f, dialect=my_dialect)
"""
CSV房源选项
delimiter
lineterminator
quotechar
quoting
skipinitialspace
doublequote
escapechar
"""    

# 6.1.4 JSON数据
fs()
obj = """
{
    "name":"Wes",
    "places_lived":[
        "United States",
        "Spain",
        "Germany"],
    "pet":null,
    "siblings":[{
            "name": "Scott",
            "age":30,
            "pets":["Zeus", "Zuko"
            ]},
        {
            "name":"Katie",
            "age":38,
            "pets":["Sixes", "Stache", "Cisco"
            ]}]
}
"""
result = json.loads(obj)
pprint(result)
fs()
asjson = json.dumps(result)
pprint(asjson)

fs()
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
pprint(siblings)

fs()
data = pd.read_json('examples/example.json')
pprint(data)

fs()
print(data.to_json())
print(data.to_json(orient='records'))


# 6.1.5 XML和HTML：网络抓取
fs()
# http://www.mat.info/developers/down_load.html

# 6.1.5.1 使用lxml.objectify解析XML


