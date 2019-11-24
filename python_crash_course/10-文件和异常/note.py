# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/11/21 13:50
"""

def fs():
	print("*" * 40)

filename = "D:/data/pcc/chapter_10/pi_digits.txt"

with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip())

fs()
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

fs()
with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())

fs()
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))

fs()
filename_one = "D:/data/pcc/chapter_10/pi_million_digits.txt"
with open(filename_one) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

fs()
with open(filename_one) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million ditits of pi!")
else:
	print("Your birthday does not appears in the first million ditits of pi.")