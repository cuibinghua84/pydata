# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:49:54 2019

@author: p_bhcui
"""

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == 'swo':
        break
print("Access granted.")