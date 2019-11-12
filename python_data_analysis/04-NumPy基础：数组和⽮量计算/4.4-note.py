# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.4-note.py
@time: 2019/11/12 10:51
"""

import numpy as np

# 4.4 使用数组进行文件输入和输出
# np.save np.load
arr = np.arange(10)
# print(arr)
np.save('some_array', arr)

print(np.load('some_array.npy'))


np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])