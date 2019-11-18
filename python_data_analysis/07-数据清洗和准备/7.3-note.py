# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:59:14 2019

@author: p_bhcui
"""

import re
from pprint import pprint

def fs():
    print("*" * 40)


# 7.3 字符串操作
# 7.3.1 字符串对象方法
val = 'a, b, guido'
print(val.split(', '))

fs()
pieces = [x.strip() for x in val.split(',')]
print(pieces)

fs()
first, second, third = pieces
print(first + '::' + second + '::' + third)
print('::'.join(pieces))

fs()
print('guido' in val)
print(val.index(', '))
print(val.find(':'))
print(val.count(','))
print(val.replace(',', '::'))
print(val.replace(', ', ''))
"""
Python内建字符串方法
count
endswith
startwith
join
index
find
rfind
replace
strip rstrip lstrip
split
lower
upper
casefold
ljust rjust
"""

# 7.3.2 正则表达式
fs()
text = "foo    bar\t baz  \tque"
print(re.split('\s+', text))

fs()
regex = re.compile('\s+')
print(regex.split(text))

fs()
print(regex.findall(text))

fs()
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
regex = re.compile(pattern, flags=re.IGNORECASE)
pprint(regex.findall(text))

fs()
m = regex.search(text)
print(m)
print(text[m.start():m.end()])

print(regex.match(text))

print(regex.sub('REDACTED', text))

# 7.3.3 pandas中向量化字符串函数


