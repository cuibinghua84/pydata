# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.2-传递实参.py
@time: 2019/11/1 13:38
"""

print("*" * 50)
# 8.2.1 位置实参
def describe_pet(pet_name, animal_type='dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 8.2.2 关键字实参
print("*" * 50)
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 8.2.3 默认值
print("*" * 50)
describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')

# 8.2.4 等效的函数调用
print("*" * 50)

# 8.2.5 避免实参错误
print("*" * 50)

