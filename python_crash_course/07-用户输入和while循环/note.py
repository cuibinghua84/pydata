# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:30:22 2019

@author: p_bhcui
"""


def fs():
    print("*" * 40)


# 7.1 函数input()的工作原理
# message = input("Tell me something, and I will rrepeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name.title() + "!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print("\nHello, " + name.title() + "!")

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height > 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even.")
# else:
#     print("\nThe number " + str(number) + " is odd.")

# 7.2 while循环简介
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# fs()
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program."
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

fs()
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 7.3 使用while循环来处理列表和字典
fs()
print("在列表之间移动元素")
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe follwing users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

fs()
# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

fs()
# 使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

"""
1、如何在程序中使用input()来让用户提供信息
2、如何处理文本和数字输入，以及如何使用while让程序按用户的要求不断地运行
3、多种控制while循环流程的方式
4、设置活动标志、使用break语句以及使用continue语句
5、如何使用while循环在列表中移动元素，以及如何从列表中删除所有包含特定值的元素
6、如何结合使用while循环和字典
"""
