# -*- coding: utf-8 -*-
"""
@author: 东风
@file: write_message.py
@time: 2019/11/4 16:01
"""

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
