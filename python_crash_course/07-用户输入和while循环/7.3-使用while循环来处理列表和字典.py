# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.3-使用while循环来处理列表和字典.py
@time: 2019/11/1 13:38
"""

# 7.3.1 在列表之间移动元素
# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
print("*" * 50)
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())


# 7.3.2 删除包含特定值的所有列表元素
print("*" * 50)
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

# 7.3.3 使用用户输入来填充字典
print("*" * 50)
responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	responses[name] = response
	repeat = input("Would you like to let another person respond?(yes/ no) ")
	if repeat == "no":
		polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")