# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 9.1-简明matplotlibAPI入门.py
@time: 2019/10/28 18:09
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

# 简单的线性图
# data = np.arange(10)
# print(data)
# plt.plot(data)

# 9.1.1 图片和子图
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# # ax4 = fig.add_subplot(2, 2, 4)
# plt.plot(np.random.randn(50).cumsum(), 'k--')
# _ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

# fig, axes = plt.subplots(2, 3)
# print(axes)
"""
pyplot.subplots选项
nrows
ncols
sharex
sharey
subplot_kw
**fig_kw
"""

# 9.1.1.1 调整子图周围的间距
# fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
# plt.subplots_adjust(wspace=0, hspace=0)

plt.plot(randn(30).cumsum(), 'ko--')


plt.show()

