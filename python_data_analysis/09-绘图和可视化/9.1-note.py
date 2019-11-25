# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:51:38 2019

@author: p_bhcui
"""

import matplotlib.pyplot as plt
import numpy as np

def fs():
    print("*" * 40)

# data = np.arange(10)
# print(data)
# plt.plot(data)


fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(np.random.randn(50).cumsum(), 'k--')

_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.random.randn(30), np.arange(30) + 3 * np.random.randn(30))


fig, axes = plt.subplots(2, 3)
axes

fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)

