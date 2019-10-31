# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 3.1-列表是什么.py
@time: 2019/10/30 10:57
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 3.1.1 访问列表元素
print(bicycles[0].title())

# 3.1.2 索引从0而不是从1开始
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

# 3.1.3 使用列表中的各个值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
