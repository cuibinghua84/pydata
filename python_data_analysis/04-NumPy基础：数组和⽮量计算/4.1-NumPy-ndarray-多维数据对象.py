# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.1-NumPy-ndarray-多维数据对象.py
@time: 2019/10/11 23:03
"""
import numpy as np
from pprint import pprint

"""
Numpy的核心特征之一就是N-维数组对象——ndarray
ndarray是Python中一个快速、灵活的大型数据集容器
数据允许你使用类似标量的操作语法在整块数据上进行数学计算
"""
# 感受NumPy如何进行批量计算
# 生成随机数组
data = np.random.rand(2, 3)
pprint(data)
pprint(data * 10)
pprint(data + data)

# ndarray是一个通用的多维同类数据容器，即它包含的每一个元素均为相同类型；
# 每一个数组都有一个shape属性，用来表征数组每一维度的数量
# 每一个数组都有一个dtype属性，用来描述数组的数据类型
print(data.shape)
print(data.dtype)

# 4.1.1 生成ndarray
# 1 使用array函数：可接受任意的序列型对象
# 如列表转换
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
pprint(arr1)
# 嵌套序列，如等长度的列表，将会自动转换成多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
pprint(arr2)
# 通过ndim和shape属性来确定是否为二维数组
pprint(arr2.ndim)
pprint(arr2.shape)
pprint(arr2.dtype)
# 2 zeros可以一次性创造全是0数组
pprint(np.zeros(10))
pprint(np.zeros((3, 6)))
# 3 ones可以一次性创造全是1数组
pprint(np.ones(10))
# 4 empty则可以创建一个没有初始化值的数组
pprint(np.empty((2, 3, 2)))

# arange是Python内建函数的数组版
pprint(np.arange(15))

"""
以下是标注数组的生成函数
如没有特殊指明，NumPy默认的数据类型是float64（NumPy专注于数值计算）
array：将输入数据转换为ndarray
asarray：将输入转化为ndarray，但如果输入是ndarray则不再复制
arange：Python内建函数range的数组版，返回一个数组
"""

# 4.1.2 ndarray的数据类型


# 4.1.3 NumPy数组算术

# 4.1.4 基础索引与切片

# 4.1.4.1 数组的切片索引

# 4.1.5 布尔索引

# 4.1.6 神奇索引

# 4.1.7 数组转置和换轴




