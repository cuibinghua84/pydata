# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/11/20 14:43
"""


def fs():
    print("*" * 40)


# 6.1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2 使用字典
fs()
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

fs()
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

fs()
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

fs()
alien_0 = {'x_position': 2, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

fs()
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

fs()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite languages is " + favorite_languages['sarah'].title() + ".")

# 6.3 遍历字典
fs()
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

fs()
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is + " + language.title() + ".")

fs()
for name in favorite_languages.keys():
    print(name.title())

fs()
friend = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friend:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

fs()
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

fs()
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

fs()
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

# 6.4 嵌套
fs()
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

fs()
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

fs()
aliens = []
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:5]:
    print(alien)
print("...")

fs()
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with topping in pizza['toppings")
for topping in pizza['toppings']:
    print("\t" + topping)

fs()
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

fs()
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
    print("\nUsername: " + username.title())
    full_name = user_info['first'] + " " + user_info['last']

    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

"""
1、如何定义字典，以及如何使用存储在字典中的信息
2、如何访问和修改字典中的元素，以及如何遍历字典中的所有信息
3、如何遍历字典中的所有键-值对，所有的键和所有的值
4、如何在列表中嵌套字典、在字典中嵌套列表以及在字典中嵌套字典
"""
