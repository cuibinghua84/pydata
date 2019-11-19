# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:12:21 2019

@author: p_bhcui
"""

from pprint import pprint

def fs():
    print("*" * 40)

# 2.1
print("Hello Python world!")

# 2.2 变量
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)

# 2.3 字符串
name = "ada lovELace"
print(name.title())
print(name.upper())
print(name.lower())

fs()
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

fs()
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

fs()
favorite_language = ' python '
pprint(favorite_language)
pprint(favorite_language.rstrip())
pprint(favorite_language.lstrip())
pprint(favorite_language.strip())

fs()
print("动手试一试")
name = "df"
message = "Hello " + name.title() + ", would you like to learn some Python today?"
print(message)
print(4 + 4)
print(8 - 4)
print(4 * 2)
print(16 // 2)

fs()
number = 888
print("My favorite number is " + str(number))

import this
"""
1、如何使用变量
2、如何创建描述性变量名以及如何消除名称错误和语法错误
3、字符串是什么，以及如何使用小写、大写和首字母大写方式显示字符串
4、使用空白连显示整洁的输出，以及如何剔除字符串中多余的空白
5、如何使用整数和浮点数
6、使用数值数据时需要注意的意外行为
"""
