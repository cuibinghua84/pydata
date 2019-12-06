# -*- coding: utf-8 -*-
"""
@author: 东风
@file: magic8Ball2.py
@time: 2019/12/6 18:00
"""

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
