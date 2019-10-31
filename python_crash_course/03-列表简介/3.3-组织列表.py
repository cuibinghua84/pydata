# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 3.3-组织列表.py
@time: 2019/10/30 10:57
"""

# 3.3.1 sort()方法对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# 3.3.2 sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list: ")
print(cars)
print("\nHere is the sorted list: ")
print(sorted(cars))
print("\nHere is the original list again: ")
print(cars)

# 3.3.3 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print()
print(cars)
cars.reverse()
print(cars)


# 3.3.4 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))