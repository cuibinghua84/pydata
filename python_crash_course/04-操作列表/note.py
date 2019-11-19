# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:29:47 2019

@author: p_bhcui
"""

def fs():
	print("*" * 40)

# 4.1 遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

# 4.2 避免缩进错误
# 忘记缩进、忘记缩进额外的代码行、不必要的缩进、循环后不必要的缩进、遗漏了冒号

# 4.3 创建数值列表
fs()
for value in range(1, 6):
	print(value)

fs()
numbers = list(range(1, 6))
print(numbers)

fs()
even_numbers = list(range(2, 11, 2))
print(even_numbers)

fs()
squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)

fs()
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

fs()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

fs()
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 4.4 使用列表的一部分
fs()
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

fs()
print("Here are the first three players on my team: ")
for player in players[:3]:
	print(player.title())

fs()
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]



# 4.5 元组

# 4.6 设置代码格式






"""
1、如何高效地处理列表中的元素
2、如何使用for循环遍历列表，Python如何根据缩进来确定程序的结构以及如何避免一些常见的缩进错误
3、如何创建简单的数字列表，以及可对数字列表执行的一些操作
4、如果通过切片来使用列表的一部分和复制列表
5、学习元组
6、如何设置格式

"""