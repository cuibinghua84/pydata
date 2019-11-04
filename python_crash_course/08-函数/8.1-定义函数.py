# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.1-定义函数.py
@time: 2019/11/1 13:38
"""
print("*" * 50)
def greet_user():
	print("Hello!")
greet_user()

# 8.1.1 向函数传递信息
print("*" * 50)
def greet_user_0(username):
	print("Hello, " + username.title() + "!")
greet_user_0('jesse')

# 8.1.2 实参和形参
print("*" * 50)
