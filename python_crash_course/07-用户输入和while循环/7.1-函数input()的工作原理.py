# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.1-函数input()的工作原理.py
@time: 2019/11/1 13:38
"""

# message = input("Tell me something , and I will repeat it back to you: ")
# print(message)

# 7.1.1 编写清晰的程序
print("*" * 50)
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

print("*" * 50)
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, " + name + "!")


# 7.1.2 使用int()来获取数值输入
# print("*" * 50)
# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
# 	print("\nYou're tall enough to ride!")
# else:
# 	print("\nYou'll be able to ride when you're a little older.")

print("*" * 50)


# 7.1.3 求模运算符
print("*" * 50)
# 判断奇偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")

print("*" * 50)

