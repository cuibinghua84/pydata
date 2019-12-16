# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/16 10:17
"""

from pprint import pprint
import numpy as np


def fs():
    print("*" * 50)


"""
In [1]: import numpy as np

In [2]: my_arr = np.arange(1000000)
In [3]: my_list = list(range(1000000))

In [4]: %time for _ in range(10): my_arr2 = my_arr * 2
Wall time: 18 ms

In [5]: %time for _ in range(10): my_list2 = [x * 2 for x in my_list]
Wall time: 930 ms
"""

# 4.1 NumPy ndarray：多维数组对象

# 生成随机数组
data = np.random.randn(2, 3)
pprint(data)
fs()

# 给data加上一个数学操作
# 所有的元素同时乘以10
pprint(data * 10)
fs()

# 数组中的对应元素进行相加
pprint(data + data)
fs()

# shape属性：用来表征数组每一维度的数量
# dtype属性：用来描述数组的数据类型
print(data.shape)
print(data.dtype)

fs()
# 4.1.1 生成ndarray
# 使用array函数
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
pprint(arr1)

# 嵌套序列，自动转换成多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
pprint(arr2)

fs()
# ndim和shape属性
print(arr2.ndim)
print(arr2.shape)
print(arr1.dtype)
print(arr2.dtype)

fs()
# zeros创建一次性全是0数组
pprint(np.zeros(10))
pprint(np.zeros((3, 6)))
# ones一次性创造全是1数组
pprint(np.ones(10))
pprint(np.ones((3, 6)))
# empty创造一个没有初始化数值的数组
# 要创建高维数组，需要为shape传递一个元组
pprint(np.empty((2, 3, 2)))

fs()
# arange是Python内建函数range的数组版
pprint(np.arange(15))

# NumPy专注于数值计算，如果没有特别指明的话，默认的数据类型是float64
# 数组生成函数
"""
array
asarray
arange
"""

# 4.1.2 ndarray的数据类型
fs()
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)
"""
NumPy数据类型
"""

fs()
# astype显式地转换数组的数据类型
# 整数转成浮点数
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

# 浮点数转成整数，小数点后的部分将被取消
fs()
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
pprint(arr)
print(arr.dtype)
pprint(arr.astype(np.int32))

# 如果一个数组，里面的元素都是表达数字含义的字符串，可通过astype将字符串转换为数字
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
pprint(numeric_strings.astype(float))

fs()
# NumPy可以使用相同别名来表征与Python精度相同的Python数据类型
int_array = np.arange(10)
# pprint(int_array)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
# pprint(calibers)
pprint(int_array.astype(calibers.dtype))
print(calibers.dtype)

fs()
# 使用类型代码传入数据类型
empty_uint32 = np.empty(8, dtype='u4')
pprint(empty_uint32)
# 使用astype时总是生成一个新的数组，即使你传入的dtype与之前一样

# 4.1.3 NumPy数组算术
fs()
# 数组之所以重要是因为它允许你进行批量操作而无须任何for循环，即向量化
# 任何在两个等尺寸数组间的算术操作都应用了逐元素操作的方式
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
pprint(arr)
pprint(arr * arr)
pprint(arr - arr)

# 带有标量计算的算术操作，会把计算参数传递给数组的每一个元素
fs()
pprint(1 / arr)
pprint(arr ** 0.5)

# 同尺寸数组之间的比较，会产生一个布尔值数组
fs()
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
pprint(arr2)
pprint(arr2 > arr)

# 不同尺寸的数组间的操作，将会用到广播特性

fs()
# 4.1.4 基础索引与切片
arr = np.arange(10)
pprint(arr)
pprint(arr[5])
pprint(arr[5:8])
arr[5:8] = 12
pprint(arr)

# 数组的切片是原数组的视图，即数据并不是被复制了，任何对于视图的修改都会反映到原数组上
fs()
arr_slice = arr[5:8]
pprint(arr_slice)

# 改变arr_slice，变也恩惠体现在原数组上
arr_slice[1] = 12345
pprint(arr)

# 不写切片值的[:]将会引用数组的所有值
arr_slice[:] = 64
pprint(arr)

fs()
# 二维数组中，每个索引值对应的元素不再是一个值，而是一个一维数组
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pprint(arr2d[2])
pprint(arr2d[0][2])

fs()
# 多维数组，返回的对象将是一个降低一个维度的数组
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
pprint(arr3d)

pprint(arr3d[0])

fs()
# 标量和数组都可以传递给arr3d[0]
old_values = arr3d[0].copy()
pprint(old_values)
arr3d[0] = 42
pprint(arr3d)
arr3d[0] = old_values
pprint(arr3d)

fs()
# 返回一个一维数组
pprint(arr3d[1, 0])

fs()
# 以上步骤分解
x = arr3d[1]
pprint(x)
pprint(x[0])

fs()
# 4.1.4.1 数组的切片索引
pprint(arr)
pprint(arr[1:6])

# 二维数组切片
fs()
pprint(arr2d)
pprint(arr2d[:2])
pprint(arr2d[:2, 1:])

fs()
# 索引和切片混合
pprint(arr2d)
# 第二行前两列
pprint(arr2d[1, :2])
# 第三列前两行
pprint(arr2d[:2, 2])
# 单独冒号
pprint(arr2d[:, 1:])

fs()
# 对切片赋值时，整个切片都会重新赋值
arr2d[:2, 1:] = 0
pprint(arr2d)
