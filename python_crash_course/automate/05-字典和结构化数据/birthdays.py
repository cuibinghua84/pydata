# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:55:07 2019

@author: p_bhcui
"""

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (black to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday? ')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')


