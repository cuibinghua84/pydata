#!/usr/bin/env python
# coding: utf-8

import numpy as np
from pprint import pprint


# 4.3使用数组进行面向数组编程
# 向量化：利用数组表达式来替代显式循环的方法

# 计算函数sqrt(x^2 + y ^ 2)的值
points = np.arange(-5, 5, 0.01)
# pprint(points)
xs, ys = np.meshgrid(points, points)
# pprint(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
pprint(z)

