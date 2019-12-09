# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:05:08 2019

@author: p_bhcui
"""

import pprint

message = 'It was a bright cold day in April, and the colocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)
pprint.pprint(count)