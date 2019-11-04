# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.2-while循环简介.py
@time: 2019/11/1 13:38
"""

# 7.2.1 使用while循环
# print("*" * 50)
# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number += 1

# 7.2.2 让那用户选择何时退出
# print("*" * 50)
# prompt = "\nThe me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(message)
# print("*" * 50)


# 7.2.3 使用标志
# print("*" * 50)
# prompt = "\nThe me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
# 	message = input(prompt)
# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)



# 7.2.4 使用break退出循环
# print("*" * 50)
# prompt = "\nThe me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# while True:
# 	city = input(prompt)
# 	if city == 'quit':
# 		break
# 	else:
# 		print("I'd love to go to " + city.title() + "!")

# 7.2.5 在循环中使用continue
print("*" * 50)
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

print("*" * 50)

# 7.2.6 避免无限循环
print("*" * 50)
print("*" * 50)
