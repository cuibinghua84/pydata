# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/20 9:50
"""

from pprint import pprint
from datetime import datetime
from datetime import timedelta


def fs():
    print("*" * 50)


# 11.1 日期和时间数据的类型工具
now = datetime.now()
pprint(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)

fs()
delta = datetime(2020, 1, 1) - datetime(2019, 12, 29)
print(delta)
print(delta.days)
print(delta.seconds)

fs()
start = datetime(2011, 1, 7)
pprint(start + timedelta(12))
pprint(start - 2 * timedelta(12))
"""
datetime模块中的类型
date    使用公历日历存储日历日期（年，月，日）
time    将时间存储为小时，分钟，秒和微妙
datetiime 存储日期和时间
timedelta 表示两个datetime值之间的差（如日，秒和微妙）
tzinfo  用于存储时区信息的基本类型
"""

# 11.1.1 字符串与datetime互相转换





# 11.2 时间序列基础

# 11.3 日期范围、频率和移位

# 11.4 时区处理

# 11.5 时间区间和区间算术

# 11.6 重新采样与频率转换

# 11.7 移动窗口函数
