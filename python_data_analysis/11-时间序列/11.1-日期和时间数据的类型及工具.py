# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 11.1-日期和时间数据的类型及工具.py
@time: 2019/10/28 18:12
"""

from datetime import datetime
from pprint import pprint


def fs():
    print("*" * 40)


now = datetime.now()
pprint(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)


