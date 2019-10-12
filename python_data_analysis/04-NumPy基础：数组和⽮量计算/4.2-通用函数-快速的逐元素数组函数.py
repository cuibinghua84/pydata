# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.2-通用函数-快速的逐元素数组函数.py
@time: 2019/10/12 17:19
"""
import numpy as np
from pprint import pprint

# print("\n高纬度数组，transpose可以接受包含轴编号的元组，用于置换轴")
# arr = np.arange(16).reshape((2, 2, 4))
# pprint(arr)
# pprint(arr.transpose((1, 0, 2)))

# print("\nswapaxes接收一堆轴编号作为参数，并对轴进行调整用于重组数据")
# print("swapaxes返回的是数据的视图，而没有对数据进行复制")
# pprint(arr)
# pprint(arr.swapaxes(1, 2))



