# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:23:32 2019

@author: p_bhcui
"""

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only): ')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')