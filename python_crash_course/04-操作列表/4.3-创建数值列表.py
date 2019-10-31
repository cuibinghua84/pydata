# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.3-创建数值列表.py
@time: 2019/10/30 10:59
"""

# 4.3.1 使用函数range()
for value in range(1, 6):
	print(value)
print()

# 4.3.2 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

print()
squares = []
for value in range(1, 11):
	# print(value)
	square = value ** 2
	# print(square)
	squares.append(square)
print(squares)

print()
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

# 4.3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)