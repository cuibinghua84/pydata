# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.2-使用字典.py
@time: 2019/11/1 13:37
"""

# 6.2.1 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

# 6.2.2 添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 6.2.4 修改字典中的值
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " +alien_0['color'] + ".")

print()
alien_0 = {'x_position': 1, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# 这个外星人的速度一定很快
	x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 6.2.5 删除键-值对
print("*" * 50)
alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
print(alien_0)
del alien_0['color']
print(alien_0)

# 6.2.6 由类似对象组成的字典
print("*" * 50)
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
print("Sarah's favorite languages is " + favorite_languages['sarah'].title() + ".")

