# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.4-使用列表的一部分.py
@time: 2019/10/30 10:59
"""

# 4.4.1 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# 4.4.2 遍历切片
print("Here are the first three players on my team: ")
for player in players[:3]:
	print(player.title())

# 4.4.3 复制列表
print()
my_foods = ['pizza', 'falafel', 'carrotcake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)
