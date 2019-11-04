# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.4-传递列表.py
@time: 2019/11/1 13:38
"""

print("*" * 50)
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'tr', 'margot']
greet_users(usernames)

print("*" * 50)
# 8.4.1 在函数中修改列表
# unprinted_designs = ['iphone case', 'robot  pendant', 'dodecahedron']
# completed_models = []
# while unprinted_designs:
# 	current_design = unprinted_designs.pop()
# 	print("Printing model: " + current_design)
# 	completed_models.append(current_design)
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
# 	print(completed_model)

# 优化1
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " +current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# 8.4.2 禁止函数修改列表
print("*" * 50)

# 8.4.3 
print("*" * 50)


print("*" * 50)