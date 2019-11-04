# -*- coding: utf-8 -*-
"""
@author: 东风
@file: file_reader.py
@time: 2019/11/4 15:24
"""

path = "D:/data/pcc/chapter_10/pi_digits.txt"
with open(path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print("*" * 50)
with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())

print("*" * 50)
with open(path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

print("*" * 50)
with open(path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
