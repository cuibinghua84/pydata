# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.3-字符串操作.py
@time: 2019/10/25 17:35
"""

# 7.3.1 字符串对象方法
val = 'a, b, guido'
print(val.split(','))

print("*" * 60)
pieces = [x.strip() for x in val.split(',')]
print(pieces)

print("*" * 60)
first, second, third = pieces
print(first + '::' + second + "::" + third)
print('::'.join(pieces))

print("*" * 60)
# find和index的区别在于index在字符串没有找到时会抛出一个异常
print('guido' in val)
print(val.index(','))
print(val.find(":"))

print("*" * 60)
print(val.count(","))

print("*" * 60)
print(val.replace(',', '::'))
print(val.replace(',', ''))

"""
python内建字符串方法
count
endswith
startswith
join
index
find
rfind
replace
strip,rstrip,lstrip
split
lower
upper
casefold
ljust,rjust
"""


# 7.3.2 正则表达式
"""
正则表达式方法
findall
finditer
match
search
split
sub,subn
"""

# 7.3.3 pandas中的向量化字符串函数
"""pandas更多字符串方法
cat 		根据可选的分隔符按元素粘合字符串
contains 	返回是否含有某个模式/正则表达式的布尔值数组
count 		模式出现次数的计数
extract 	使用正则表达式从字符串Series中分组抽取一个或多个字符串；返回的结果是每个分组形成一列的DataFrame
endswith 	等价于对每个元素使用x.endwith(模式)"""

