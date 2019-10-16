# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.7-示例-随机漫步.py
@time: 2019/10/12 17:39
"""
import random
import numpy as np
import matplotlib.pyplot as plt

# 纯Python实现
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
plt.plot(walk[:100])
plt.show()