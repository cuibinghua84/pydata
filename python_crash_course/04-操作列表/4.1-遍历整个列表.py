# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.1-遍历整个列表.py
@time: 2019/10/30 10:58
"""

# 4.1.1 深入地研究循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

# 4.1.2 在for循环中执行更多的操作
# 4.1.3 在for循环结束后执行一些操作
print()
for magician in magicians:
	print(magician.title() + ", that was a greate trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")


