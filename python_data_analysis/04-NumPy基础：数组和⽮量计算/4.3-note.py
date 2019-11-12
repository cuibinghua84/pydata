#!/usr/bin/env python
# coding: utf-8

import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt

# 4.3使用数组进行面向数组编程
# 向量化：利用数组表达式来替代显式循环的方法

# 计算函数sqrt(x^2 + y ^ 2)的值
points = np.arange(-5, 5, 0.01)
# pprint(points)
xs, ys = np.meshgrid(points, points)
# pprint(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
# pprint(z)

# plt.imshow(z, cmap=plt.cm.gray)
# plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()

# 4.3.1 将条件脱机作为数组操作
# numpy.where
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# cond为True显示xarr，否则yarr
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
pprint(result)

# 另外一种方式
result = np.where(cond, xarr, yarr)
pprint(result)

arr = np.random.randn(4, 4)
pprint(arr)
pprint(arr > 0)

pprint(np.where(arr > 0, 2, -2))
pprint(np.where(arr > 0, 2, arr))

# 4.3.2 数学和统计方法
print("*" * 40)
arr = np.random.randn(5, 4)
pprint(arr)

# 求平均值:mean()
"""
axis：不设置 返回一个实数
axis=0，对各列求均值
axis=1，对各行求均值
"""
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
print(arr.mean(axis=0))
print(arr.mean(axis=1))

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())
print(arr.cumprod())

print("*" * 40)
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
pprint(arr)
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))
"""
基础数组统计方法
sum:沿着轴向计算所有元素的累和，0长度的数据，累和为0
mean：数学平均，0长度的数组平均值为NaN
std,var：标准差和方差，可以选择自由度调整（默认分母是n）
min,max：最小值和最大值
argmin,argmax最小值和最大值的位置
cumsum：从0开始元素累积和
cumprod：从1开始元素累积和
"""

# 4.3.3 布尔值数组的方法
print("*" * 40)
arr = np.random.randn(100)
# pprint(arr)
pprint((arr > 0).sum())  # 正值的个数

# any：检查数组中是否至少有一个True   all：检查是否每个值都是True
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())

print("*" * 40)
# 4.3.4排序
# sort方法按位置排序
# sort方法返回的是已经排序好的数组拷贝，而不是对原数组按位置排序
arr = np.random.randn(6)
pprint(arr)
arr.sort()
pprint(arr)

print("*" * 40)
arr = np.random.randn(5, 3)
pprint(arr)
arr.sort(axis=1)
pprint(arr)

print("*" * 40)
# 数组的分位数
large_arr = np.random.randn(1000)
# pprint(large_arr)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])

print("*" * 40)
# 4.3.3 唯一值与其他集合逻辑
# np.unique 返回数组中唯一值排序后形成的数组
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
pprint(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))

pprint(sorted(set(ints)))

# np.in1d：检查一个数组中的值，是否在另外一个数组中，返回布尔值数组
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))
"""
数组的集合操作
unique(x)：计算x的唯一值，并排序
interset1d(x, y)：计算x和y的交集，并排序
union1d(x, y)：计算x和y的并集，并排序
in1d(x, y)：计算x中的元素是否包含在y中，返回一个布尔值数组
setdiff1d(x, y)：差集，在x中但不在y中的x的元素
setxor1d(x, y)：异或集，在x或y中，但不属于x，y交集的元素

"""

