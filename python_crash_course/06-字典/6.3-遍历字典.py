# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.3-遍历字典.py
@time: 2019/11/1 13:37
"""

# 6.3.1 遍历所有的键-值对
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

print("*" * 50)
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name, langages in favorite_languages.items():
	print(name.title() + "'s favorite language is " + langages.title() + ".")

# 6.3.2 遍历字典中的所有键
print("*" * 50)
for name in favorite_languages.keys():
	print(name.title())

print("*" * 50)


# 6.3.3 按顺序遍历字典中的所有键
print("*" * 50)

# 6.3.4 遍历字典中的所有值
print("*" * 50)
