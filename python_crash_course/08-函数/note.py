# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/11/21 13:50
"""


def fs():
    print("*" * 40)


# 8.1 定义函数
def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user('jesse')

# 8.2 传递实参
# 位置实参
fs()


def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(animal_type='hamster', pet_name='willie')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 默认值
fs()


def describe_pet_one(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_one(pet_name='willie')
describe_pet_one('willie')
describe_pet_one(pet_name='harry', animal_type='hamster')

# 等效的函数调用
fs()
describe_pet_one('willie')
describe_pet_one(pet_name='willie')
describe_pet_one('harry', 'hamster')
describe_pet_one(pet_name='harry', animal_type='hamster')
describe_pet_one(animal_type='hamster', pet_name='harry')

# 8.3 返回值
fs()


def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# 实参变成可选
def get_formatted_name_one(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_one('john', 'lee', 'hooker')
print(musician)

fs()


def get_formatted_name_two(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name_two('jimi', 'hendrix')
print(musician)
musician = get_formatted_name_two('john', 'hooker', 'lee')
print(musician)

# 返回字典
fs()


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=36)
print(musician)

fs()

# def get_formatted_name_three(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name_three(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# 8.4 传递列表
fs()


def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


username = ['hannah', 'ty', 'margot']
greet_users(username)

# 在函数中修改列表
fs()
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design.title())
    completed_models.append(current_design)
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model.title())

fs()


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design.title())
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8.5 传递任意数量的实参
fs()


def make_pizza(size, *toppings):
    # print(toppings)
    # print("Making a pizza with the following toppings: ")
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

fs()


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in profile.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# 8.6 将函数存储在模块中
"""
导入整个模块
import pizza

导入特定函数
from pizza import make_pizza

as给函数命名
from pizza import make_pizza as mp

as给模块命名
import pizza as p

导入所有函数
from pizza import *
"""

# 8.7 函数编写指南


"""
1、如何编写函数，以及如何传递参数，让函数能够访问完成其工作所需的信息
2、如何使用位置实参和关键字实参，以及如何接受任意数量的实参
3、显示输出的函数和返回值的函数
4、如何将函数同列表、字典、if语句和while循环结合起来使用
"""
