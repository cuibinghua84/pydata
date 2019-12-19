# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/18 18:03
"""

from pprint import pprint
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as web
import sys
import csv
import json

def fs():
    print("*" * 50)


# 6.1 文本格式数据的读写
"""
pandas的解析函数
pd.read_csv
pd.read_table
pd.read_fwf()
pd.read_clipboard()
pd.read_excel
pd.read_hdf()
pd.read_html()
pd.read_json()
pd.read_msgpack()
pd.read_pickle()
pd.read_sas()
pd.read_sql()
pd.read_stata
pd.read_feather
"""
df = pd.read_csv("D:/data/pydata_book2/examples/ex1.csv")
print(df)

fs()
print(pd.read_table("D:/data/pydata_book2/examples/ex1.csv", sep=','))

fs()
print(pd.read_csv('D:/data/pydata_book2/examples/ex2.csv', header=None))

fs()
print(pd.read_csv("D:/data/pydata_book2/examples/ex2.csv", names=['a', 'b', 'c', 'd', 'message']))

fs()
names = ['a', 'b', 'c', 'd', 'message']
print(pd.read_csv('D:/data/pydata_book2/examples/ex2.csv', names=names, index_col='message'))

fs()
parsed = pd.read_csv('D:/data/pydata_book2/examples/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

fs()
result = pd.read_table("D:/data/pydata_book2/examples/ex3.txt", sep='\s+')
print(result)

fs()
result = pd.read_csv("D:/data/pydata_book2/examples/ex5.csv")
print(result)
print(pd.isnull(result))

fs()
result = pd.read_csv("D:/data/pydata_book2/examples/ex5.csv", na_values=['NULL'])
print(result)

fs()
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
print(pd.read_csv("D:/data/pydata_book2/examples/ex5.csv", na_values=sentinels))
"""
read_csv/read_table函数参数
path
sep delimier
header
index_col
names
skiprows
na_values
comment
parse_dates
keep_date_col
converters
dayfirst
"""

# 6.1.1 分块读入文本文件
fs()
pd.options.display.max_rows = 10
file = "D:/data/pydata_book2/examples/ex6.csv"
result = pd.read_csv(file)
print(result)

fs()
print(pd.read_csv(file, nrows=5))

fs()
chunker = pd.read_csv(file, chunksize=1000)
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10])

# 6.1.2 将数据写入文本格式
fs()
data = pd.read_csv("D:/data/pydata_book2/examples/ex5.csv")
print(data)
data.to_csv("D:/data/out.csv")

fs()
print(data.to_csv(sys.stdout, sep='|'))

fs()
print(data.to_csv(sys.stdout, na_rep='NULL'))

fs()
print(data.to_csv(sys.stdout, index=True, header=False))

fs()
print(data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c']))

fs()
# dates = pd.date_range('1/1/2020', periods=7)
# ts = pd.Series(np.arange(7), index=dates)
# ts.to_csv('D:/data/tseries.csv')

# 6.1.3使用分隔格式
fs()
f = open("D:/data/pydata_book2/examples/ex7.csv")
# print(f)
reader = csv.reader(f)
# print(reader)
for line in reader:
    print(line)

fs()
with open("D:/data/pydata_book2/examples/ex7.csv") as f:
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)

fs()


class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


# reader = csv.reader(f, dialect=my_dialect)
# reader = csv.reader(f, delimiter='|')
"""
CSV方言选项
csv.delimiter
csv.lineterminator
csv.quotechar
csv.quoting
csv.skipinitialspace
csv.doublequote
csv.escapechar
"""

fs()
# with open('D:/data/mydata.csv', 'w') as f:
#     writer = csv.writer(f, dialect=my_dialect)
#     writer.writerow(('one', 'two', 'three'))
#     writer.writerow(('1', '2', '3'))
#     writer.writerow(('4', '5', '6'))
#     writer.writerow(('7', '8', '9'))

# 6.1.4 JSON数据
fs()
obj = '''
{
"name": "Wes",
"places_lived" : ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 36, "pets": ["Zeus", "Zuko"]},
             {"name": "Katie", "age": 38,
             "pets": ["Sixes", "Stache", "Cisco"]}]
}
'''

result = json.loads(obj)
pprint(result)

fs()
# asjson = json.dumps(result)
# pprint(asjson)

fs()
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

fs()
data = pd.read_json('D:/data/pydata_book2/examples/example.json')
print(data)

fs()
print(data.to_json())

# 6.1.5 XML和HTML：网络抓取
# 6.1.5.1 使用lxml.objectify解析XML
# 这块的内容学习爬虫时专项学习

# 6.2 二进制格式
# 6.2.1 使用HDF5格式
# 6.2.2 读取Microsoft Excel文件
# 用到时专项学习

# 6.3 与Web API交互
# 这块的内容学习爬虫时专项学习

# 6.4 与数据库交互
# 用到时专项学习
