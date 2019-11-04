# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.4-嵌套.py
@time: 2019/11/1 13:38
"""

# 6.4.1 字典列表
print("*" * 50)
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

print("*" * 50)
aliens = []
for alien_numbers in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# print(aliens)
for alien in aliens[:5]:
	print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

print("*" * 50)
aliens = []
for alien_numbers in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# print(aliens)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'mediu'
		alien['points'] = 10
for alien in aliens[0:5]:
	print(alien)
print("...")

# 6.4.2 在字典中存储列表
print("*" * 50)
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}
print('You ordered a ' + pizza['crust'] + "-crust pizza " + "with the following toppings: ")
for topping in pizza['toppings']:
	print("\t" + topping)

print("*" * 50)
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are: ")
	for language in languages:
		print("\t" + language.title())


# 6.4.3 在字典中存储字典
print("*" * 50)
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())


print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)