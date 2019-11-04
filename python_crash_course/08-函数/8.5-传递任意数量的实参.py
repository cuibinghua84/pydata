# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.5-传递任意数量的实参.py
@time: 2019/11/1 13:38
"""
print("*" * 50)
# def make_pizza(*toppings):
# 	print(toppings)
# make_pizza('pepperoni')
# make_pizza("mushrooms", 'green peppers', 'extra cheese')

def make_pizza(*toppings):
	print("\nMaking a pizza with the following toppings: ")	
	for topping in toppings:
		print("- " + topping)
make_pizza('peppers')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参
print("*" * 50)
def make_pizzas(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)
make_pizzas(16, 'peppers')
make_pizzas(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.5.2 使用任意数量的关键字参数
print("*" * 50)
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein', location='princenton', field='physics')
print(user_profile)
