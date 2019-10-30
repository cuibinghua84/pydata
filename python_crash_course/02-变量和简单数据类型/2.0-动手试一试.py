# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 2.0-动手一试.py
@time: 2019/10/30 13:31
"""

# 2.2 动手试一试
message = "Study Python"
print(message)
message = "Study Python Python Python"
print(message)

# 2.3 动手试一试
# 2-3 个性化信息
name = 'cui'
message = ' would you like to learn some Python today?'
print(name.title() + message)

# 2-4 调整名字的大小写
name = 'cui bing hua'
print(name.lower())
print(name.upper())
print(name.title())

# 2-5、2-6 名言
name = "thomas edison"
message = ' "Where there is a will, there is a way"'
print(name.title() + " once said," + message)

# 2-7 剔除人名中的空白
name = ' cui bing hua '
print(name.lstrip())
print(name.rstrip())
print(name.strip())

