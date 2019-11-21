# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/11/20 14:43
"""


def fs():
	print("*" * 40)


# 5.1 一个简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print("\t" + car.upper())
	else:
		print(car.title())

# 5.2 条件测试
fs()
# 检查是否相等（不考虑大小写情况）、是否不相等、比较数字、检查多个条件、 检查特定值是否包含在列表中（不包含在列表中）、布尔表达式

# 5.3 if语句
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet? ")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

fs()
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

fs()
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + ".")

fs()
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5
print("Your admission cost is $" + str(price) + ".")

fs()
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese")

fs()
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
	print("\nFinished making your pizza!")

# 5.4 使用if语句处理列表
fs()
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


fs()
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 5.5 设置if语句的格式

"""
1、如何编写结果要么为True要么为False的条件测试
2、如何编写简单的if语句，if-else语句和if-elif-else结构
"""