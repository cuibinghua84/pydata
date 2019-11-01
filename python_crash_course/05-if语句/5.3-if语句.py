# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.3-if语句.py
@time: 2019/10/30 11:01
"""

# 5.3.1 简单的if语句
# 5.3.2 if-else语句
age = 20
if age >=30:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 35")

# 5.3.3 if-elif-else结构
print()
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

print()
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + ".")

# 5.3.4 使用多个elif代码块
print()
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

# 5.3.5 省略else代码块
print()
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age <65:
	price = 10
elif age >= 65:
	price = 5
print("Your admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件
print()
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making you pizza!")