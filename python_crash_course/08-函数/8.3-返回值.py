# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.3-返回值.py
@time: 2019/11/1 13:38
"""

print("*" * 50)
# 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 8.3.2 让实参变为可选的
print("*" * 50)
def get_formatted_name_midd(first_name, last_name, middle_name=''):
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name_midd('john', 'lee', 'hooker')
print(musician)

# 8.3.3 返回字典
print("*" * 50)
def build_person(first_name, last_name, age=''):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi', 'hendrix', age=36)
print(musician)

# 8.3.4 结合使用函数和while循环
print("*" * 50)
def get_formatted_name_greeter(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()
while True:
	print("\nPlease tell me your name: ")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name_greeter(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

