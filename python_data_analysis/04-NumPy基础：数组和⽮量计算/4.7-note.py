# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.7-note.py
@time: 2019/11/12 10:56
"""

import numpy as np
from pprint import pprint
from numpy.linalg import inv, qr
import random
import matplotlib.pyplot as plt

# 示例：随机漫步
# 纯Python实现一个1000步的随机漫步
# position = 0
# walk = [position]
# steps = 1000
# for i in range(steps):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
# plt.plot(walk[:1000])
# plt.show()

# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)
# steps = np.where(draws > 0, 1, -1)
# walk = steps.cumsum()
# print(walk.min())
# print(walk.max())
# print((np.abs(walk) >= 10).argmax())

nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
pprint(walks)
print(walks.max())
print(walks.min())

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())
crosing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crosing_times.mean())

