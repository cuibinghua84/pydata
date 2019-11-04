# -*- coding: utf-8 -*-
"""
@author: 东风
@file: pi_string.py
@time: 2019/11/4 15:56
"""

path = "D:/data/pcc/chapter_10/pi_million_digits.txt"
with open(path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
# print(pi_string[:52] + "...")
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

