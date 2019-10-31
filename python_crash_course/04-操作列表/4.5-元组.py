# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.5-元组.py
@time: 2019/10/30 10:59
"""

# 4.5.1 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 4.5.2 遍历元组中的所有值
print()
for dimension in dimensions:
	print(dimension)

# 4.5.3 修改元组办理
print()
print("Original dimensions: ")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions: ")
for dimension in dimensions:
	print(dimension)