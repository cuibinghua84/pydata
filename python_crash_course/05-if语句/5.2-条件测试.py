# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.2-条件测试.py
@time: 2019/10/30 11:00
"""

# 5.2.1 检查是否相等： 一个等号(=)是赋值；两个等号(==)是发问

# 5.2.2 检查是否相等时不考虑大小写：lower()

# 5.2.3 检查是否不相等： !=

# 5.2.4 比较数字：可也用各种数学比较

# 5.2.5 检查多个条件
# 1 使用and检查多个条件
# 2 使用or检查多个条件

# 5.2.6 检查特定值是否包含在列表中：in

# 5.2.7 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

# 5.2.8 布尔表达式：True False


