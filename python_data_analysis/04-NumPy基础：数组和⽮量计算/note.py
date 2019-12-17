# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/16 10:17
"""

from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt


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

# 4.1.5 布尔索引
fs()
# numpy.random的randn函数来生成一些随机正态分布的数据
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
pprint(names)
pprint(data)

# 数组的比较操作也是可以向量化的；布尔数组的长度必须和数组轴索引长度一致
# names和data数组中的一行相对应，并且我们想要选中所有的'Bob'对应的行
pprint(names == 'Bob')
# 在索引数组时可以传入布尔值数组
pprint(data[names == 'Bob'])
pprint(data[names == 'Bob', 2:])
pprint(data[names == 'Bob', 3])

# 使用!=或 ~对条件取反
fs()
pprint(names != 'Bob')
pprint(data[(names != 'Bob')])
pprint(data[~(names == 'Bob')])

fs()
# ~符号可以在想要对一个通用条件进行取反时使用
cond = names == 'Bob'
pprint(data[cond])
print()
pprint(data[~cond])

fs()
# 对布尔值条件进行联合：&  |
pprint(names)
mask = (names == 'Bob') | (names == 'Will')
pprint(mask)

fs()
# 用常识来设置布尔值数组的值
pprint(data)
# 将data中所有的负值设置为0
data[data < 0] = 0
pprint(data)

# 利用一维布尔值数组对每一行设置数值
fs()
data[names != 'Joe'] = 7
pprint(data)

fs()
# 4.1.6 神奇索引
# 用于描述使用整数数组进行数据索引
# 8x4的数组
arr = np.empty((8, 4))
# pprint(arr)
for i in range(8):
    # print(i)
    arr[i] = i
pprint(arr)

fs()
# 传递列表或数组（也可以传递负的索引）
pprint(arr[[4, 3, 0, 6]])
pprint(arr[[-3, -5, -7]])

fs()
# 传递多个索引数组时情况有些许不同，这样会根据每个索引元组对应的元素选出一个一维数组
arr = np.arange(32).reshape((8, 4))  # 生成n个自然数，并且以a行b列的数组形式显示
pprint(arr)
pprint(arr[[1, 5, 7, 2]])
pprint(arr[[1, 5, 7, 2], [0]])
pprint(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

fs()
pprint(arr[[1, 5, 7, 2]])
pprint(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
# 神奇索引与切片不同，它总是将数据复制到一个新的数组中

fs()
# 4.1.7 数组转置和换轴
# 转置是一种特殊的数据重组形式，可以返回底层数据的视图而不需要复制任何内容
# 数据拥有transpose方法，也有特殊的T属性
arr = np.arange(15).reshape((3, 5))
pprint(arr)
pprint(arr.T)

# 计算矩阵内积np.dot
fs()
arr = np.random.randn(6, 3)
pprint(arr)
pprint(np.dot(arr.T, arr))

# 高纬度的数组，transpose方法可以接收包含轴编号的元组，用于置换轴
fs()
arr = np.arange(16).reshape((2, 2, 4))
pprint(arr)
# pprint(arr.T)
pprint(arr.transpose((1, 0, 2)))

# ndarray的swapaxes方法，接收一对轴编号作为参数，并对轴进行调整用于重组数据
# swapaxes返回的是数据的视图，而没有对数据进行复制
fs()
pprint(arr)
# pprint(arr.T)
pprint(arr.swapaxes(1, 2))

fs()
# 通用函数：快速的逐元素数组函数
# 也称ufunc，是一种在ndarray数据中进行逐元素操作的函数。
arr = np.arange(10)
pprint(arr)
pprint(np.sqrt(arr))

# 二元通函数
fs()
x = np.random.randn(8)
y = np.random.randn(8)
pprint(x)
pprint(y)
# numpy.maximum逐个元素地将x和y中元素的最大值计算出来
pprint(np.maximum(x, y))

# 一元通函数返回多个数组
fs()
arr = np.random.randn(7) * 5
pprint(arr)
# modf，是Python内建函数divmod的向量化版本，返回了一个浮点数组的小数部分和整数部分
remainder, whole_part = np.modf(arr)
pprint(remainder)
pprint(whole_part)

# out参数，允许对数组按位置操作
fs()
pprint(arr)
# pprint(np.sqrt(arr))
# pprint(np.sqrt(arr, arr))
# pprint(arr)

fs()
"""
一元通函数
abs fabs
sqrt
square

二元通函数
add
subtract
multiply
divide,floor_divide
power
maximum, fmax
minimum, fmin
mod
copysign
greater,greater_equal,less,less_equal,equal, not_equal
logical_and, logical_or,logical_xor
"""

fs()
# 4.3 使用数组进行面向数组编程
# 向量化：使用NumPy数组可以使你利用简单的数组表达式完成各种数据操作任务，而无需写些大量循环
# 这种利用数组表达式来替代显示循环的方法
# 计算sqlr(x^2 +y^2)的值：
points = np.arange(-5, 5, 0.01)
# pprint(points)
xs, ys = np.meshgrid(points, points)
# pprint(xs)
# pprint(ys)

fs()
# z = np.sqrt(xs ** 2 + ys ** 2)
# # pprint(z)
# plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()

fs()
# 4.3.1 将条件逻辑作为数组操作
# numpy.where函数是三元表达式x if condition else的向量化版本
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# cond为True，取xarr，否则为yarr
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
pprint(result)

result_where = np.where(cond, xarr, yarr)
pprint(result_where)

fs()
arr = np.random.randn(4, 4)
pprint(arr)
pprint(arr > 0)
pprint(np.where(arr > 0, 2, -2))

fs()
pprint(np.where(arr > 0, 2, arr))
# np.where的数组既可以是同等大小的数组，也可以是标量

fs()
# 4.3.2 数学和统计方法
arr = np.random.randn(5, 4)
pprint(arr)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())
pprint(arr.mean(axis=1))
pprint(arr.sum(axis=0))

fs()
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
pprint(arr.cumsum())

fs()
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
pprint(arr)
pprint(arr.cumsum(axis=0))
pprint(arr.cumprod(axis=1))
"""
基础数组统计方法
sum
mean
std, var
min, max
argmin, argmax
cumsum
cumprod
"""

fs()
# 4.3.3 布尔值数组的方法
arr = np.random.randn(100)
# pprint(arr)
pprint((arr > 0).sum())

fs()
# any, all
bools = np.array([False, False, True, False])
print(bools.any())
print(bools.all())

fs()
# 4.3.4 排序
# sort
arr = np.random.randn(6)
pprint(arr)
arr.sort()
pprint(arr)

fs()
arr = np.random.randn(5, 3)
pprint(arr)
arr.sort(1)
pprint(arr)

fs()
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])

fs()
# 4.3.5 唯一值与其他集合逻辑
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
pprint(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
pprint(np.unique(ints))
print(sorted(set(names)))

fs()
values = np.array([6, 0, 0, 3, 2, 5, 6])
pprint(np.in1d(values, [2, 3, 6]))
"""
数组的集合操作
unique
intersect1d(x,y)
union1d(x,y)
in1d(x, y)
setdiff1d(x,y)
setxor1d(x, y)
"""

fs()
# 4.4 使用数组进行文件输入和输出
"""
arr = np.array(10)
np.save('some_array', arr)

np.load('some_array.npy')


"""

fs()
# 4.5 线性代数
# 4.6 伪随机数生成
# 4.7 随机漫步
