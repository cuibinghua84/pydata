# -*- coding: utf-8 -*-

import numpy as np
from pprint import pprint

"""
NumPy：（Numerical Python）是目前Python数值计算中最为重要的基础包
    ndarray，一种高效多维数组，提供了基于数组的便捷算术操作以及灵活的广播功能
    对所有数据进行快速的矩阵计算，并对内存映射文件进行操作
    线性代数、随机数生成以及傅里叶变换功能
    用于连接NumPy与C、C++和FORTRAN语言类库C语言API

作者关注的内容
    1、数据处理、清洗、构造子集、过滤、变换以及其他计算中进行快速的向量化计算
    2、常见的数组算法、比如sort、unique以及set操作等
    3、高效的描述性统计和聚合/概述数据
    4、数据排列和相关数据操作，例如对异构数据进行merge和join
    5、使用数组表达式来表明条件逻辑，代替if-elif-else条件分支的循环
    6、分组数据操作(聚合、变换以及函数式操作)
NumPy的重要性
    1、它的设计对于包含有大量数组的数据非常有效
    2、NumPy在内部将数据存储在连续的内存块上
    3、可以针对全量数据进行复杂计算而不需要些Python循环

1、NumPy ndarray: 多维数组对象
2、通用函数：快速的逐元素数组函数
3、使用数组进行面向数组编程
4、使用数组进行文件输入和输出
5、线性代数
6、伪随机数生成
7、示例：随机漫步
8、本章小结
9、
"""

# NumPy数据包含100万个整数和同样数据内容的Python列表进行比较
import numpy as np
from pprint import pprint


"""
1 NumPy本身并不提供建模和科学函数，理解NumPy的数组以及基于数组的计算将帮助你更高效地使用基于数组的工具
2 NumPy其一重要的原因：它的设计对于含有大量数组的数据非常有效
3 NumPy在内部将数据存储在连续的内存卡上，这与其他的Python内建数据结构是不同的
4 NumPy可以针对全量数组进行复杂计算而不需要写Python循环
"""

# my_arr = np.array(1000000)
# my_list = list(range(1000000))

"""
%time for _ in range(10): my_arr2 = my_arr * 2
Wall time: 0 ns
%time for _ in range(10): my_list2 = [x * 2 for x in my_list]
Wall time: 1.85 s
"""

# 4.1 NumPy ndarray：多维数组对象

# 5 ndarray是Python中一个快速、灵活的大型数据集容器。数组允许你使用类似于标量的操作语法在整块数据上进行数学计算
data = np.random.randn(2, 3)
# pprint(data)
# pprint(data * 10)
# print(data + data)

# 6 一个ndarray是一个通用的多维同类数据容器（包含的每一个元素均为相同类型）
# 7 每一个数组都有一个shape属性，用来表征数组每一维度的数量；每一个数组都有一个dtype属性，用来描述数组的数据类型
print(data.shape)
print(data.dtype)

# 4.1.1 生成ndarray
# 8 生成数组最简单的方式就是使用array函数(可接收任意的序列型对象)

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)

# 嵌套序列(包含列表的列表)，将会自动转换成多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2)

# ndim和shape：确定是否二维数组
print(arr2.ndim)
print(arr2.shape)

# 9 除非显式地指定，否则np.array会自动推断生成数组的数据类型；数据类型被存储在一个特殊的元数据中dtype
print(arr1.dtype)
print(arr2.dtype)

# 其他数组生成函数
"""
array               将输入数据(列表、元组、数组或其他序列类型)转换为ndarray。
                    要么推断出dtype，要么特别指定dtype。默认直接复制输入数据
asarray             将输入转换为ndarray，如果输入本身就是一个ndarray就不进行复制
arange              类似于内置的range，，但返回的是一个ndarray，而不是列表
ones,ones_like      根据指定的形状和dtype创建一个全是1数组。ones_like以另一个数组为参数
                    并根据其形状和dtype创建一个全是1的数组
zeros,zeros_like    类似于ones和ones_like，只不过产生的全是0数组
empty,empyt_like    创建新数组，只分配内存空间但不填充任何值
full,full_like      用fill_value中的所有值，根据指定的形状和dtype创建一个数组。full_like
                    使用另一个数组，用相同的形状和dtype创建
eye,identity        创建要给正方的NxN单位矩阵（对角线为1，其余为0）
"""
pprint(np.zeros(10))
pprint(np.zeros((3, 6)))
pprint(np.empty((2, 3, 2)))

# 10 arange是Python内建函数range的数组版
pprint(np.arange(15))

# 11 由于NumPy专注于数字计算，如果没有特别指明的话，默认的数据类型是float64

# 4.1.2 ndarray的数据类型
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)

# 12 dtype是NumPy能够与其他系统数据灵活交互的原因
"""
NumPy数据类型
int8,uint8      i1 u1
int16, uint16   i2 u2
int32,uint32    i4 u4
int64,uint64    i8 u8
float16         f2
float32         f4 f
float64         f8 d
float128        f16 g
complex64       c8 c16 c32
complex128
complex256
bool
object
string_
unicode_
"""

# astype方式显式地转换数组的数据类型
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
floar_arr = arr.astype(np.float64)
print(floar_arr.dtype)

# 如果把浮点数转换成整数，则小数点后的部分将被消除
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
pprint(arr)
pprint(arr.astype(np.int32))

# 如果数组里面的元素都是表达式数字含义的字符串，可通过astype将字符串转换为数字
numeric_string = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
# 如因某些原因导致转换失败，可使用float来代替，因为NumPy可以使用相同别名来表征与Python精度相同的Python数据类型
print(numeric_string.astype(np.float64))
print(numeric_string.astype(float))

# 也可以使用另一个数组的dtype的属性
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(int_array.astype(calibers.dtype))

# 也可以使用类型代码来传入数据类型
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)

# 使用astype总是生成一个新的数组，即使你传入的dtype与之前的一样

# # 4.1.3 NumPy数组算术
# 数组之所以重要是因为它允许你进行批量操作而无须任何for循环，即为向量化
# 在任何两个等尺度数之间的算术操作都应用了逐元素操作的方式
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr * arr)
print(arr - arr)

# 带有标量计算的算术操作，会把计算参数传递给数组的每一个元素
print(1 / arr)
print(arr ** 0.5)

# 同尺寸数组之间的比较，会产生一个布尔值数组，不同尺寸的数组间的操作，将会用到广播特性
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
pprint(arr2)
pprint(arr2 > arr)

# 4.1.4 基础索引与切片
# 一维数组
arr = np.arange(10)
pprint(arr)
pprint(arr[5])
pprint(arr[5:8])
arr[5:8] = 12
pprint(arr)

# 区别于Python的内建列表，数组的切片是原数组的视图。意味着数据并不是被复制了，任何对象与视图的修改都会被反映到原数组上
arr_slice = arr[5:8]
pprint(arr_slice)
arr_slice[1] = 12345
pprint(arr)

# 不写切片值的[:]将会引用数组的所有值
arr_slice[:] = 64
pprint(arr)


# 二维数组的索引
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pprint(arr2d[2])

# 可以通过传递一个索引的逗号分隔列表去选择单个元素
print(arr2d[2][2])
print(arr2d[2, 2])

print("*" * 40)
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
pprint(arr3d)
pprint(arr3d[0])

# 标量和数组都可以传递给arr3d[0]
print("*" * 40)
old_values = arr3d[0].copy()
arr3d[0] = 42
pprint(arr3d)
arr3d[0] = old_values
pprint(arr3d)
pprint(arr3d[1, 0])

# 步骤分解
print("*" * 40)
x = arr3d[1]
pprint(x)
pprint(x[0])

# 4.1.4.1 数组的切片索引
print("*" * 40)
pprint(arr)
pprint(arr[1:6])
pprint(arr2d)
pprint(arr2d[:2])

# 多组切片
pprint(arr2d[:2, 1:])
pprint(arr2d[1, :2])
pprint(arr2d[:2, 2])
pprint(arr2d[:, :1])

# 切片赋值
arr2d[:2, 1:] = 0
pprint(arr2d)

# 4.1.5 布尔索引
print("*" * 40)
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
pprint(names)
data = np.random.randn(7, 4)
pprint(data)
pprint(names)

# 数组的比较也可以向量化
pprint(names == 'Bob')

# 索引数组时可以传入布尔值数组
pprint(data[names == 'Bob'])

# 布尔值数组的长度必须和数组轴索引长度一致
print("*" * 40) 
pprint(data[names == 'Bob', 2:])
pprint(data[names == 'Bob', 3])

# 选择其他数据:可以使用!=或在条件表达式使用~对条件取反
print("*" * 40) 
print(names != 'Bob')
print(data[~(names == 'Bob')])

# ~符号可以在你想要对一个通用条件进行取反时使用
print("*" * 40) 
cond = names == 'Bob'
print(data[~cond])

# 选择三个名字中的两个时，可以对多个布尔值条件进行联合，使用&(and) 和 or

print("*" * 40) 
pprint(names)
mask = (names == 'Bob') | (names == 'Will')
pprint(mask)
pprint(data[mask])

# 使用布尔值索引选择数据时，总是生成数据的拷贝，即使返回的数组并没有任何变化
# 常识来设置布尔值数组的值
print("*" * 40) 
data[data < 0] = 0
pprint(data)

# 利用一维布尔值数组对每一行设置数值
print("*" * 50) 
# pprint(names)
data[names != 'Joe'] = 7
pprint(data)

# 4.1.6 神奇索引
# 术语：用于描述使用整数数据进行数据索引
print("*" * 40)
arr = np.empty((8, 4))
# pprint(arr)
for i in range(8):
    arr[i] = i
pprint(arr)

# 传递列表或数组
pprint(arr[[4, 3, 0, 6]])

# 传递负数索引
pprint(arr[[-3, -5, -7]])

# 传递多个索引数组时的情况：会根据每个索引元组对应的元素选出一个一维数组
print("*" * 40) 
arr = np.arange(32).reshape((8, 4))
pprint(arr)

print("*" * 40) 
pprint(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])


# 4.1.7 数组转置和换轴
print("*" * 40) 
# 返回的是底层数据的视图而不需要复制任何内容
# 数组拥有transpose方法，也有特殊的T属性
arr = np.arange(15).reshape((3, 5))
pprint(arr)
pprint(arr.T)
pprint(arr)

print("*" * 40) 
# 计算矩阵内积会使用np.dot
arr = np.random.randn(6, 3)
pprint(arr)
pprint(np.dot(arr.T, arr))

# 更高维的数组操作，transpose方法可以接收包含轴编号的元组，用于置换轴
print("*" * 40) 
arr = np.arange(16).reshape((2, 2, 4))
pprint(arr)
pprint(arr.transpose((1, 0, 2)))

# ndarray的swapaxes方法，接收一对轴编号作为参数，并对轴进行调整用于重组数据
# swapaxes返回的是数据的视图，而没有对数据进行复制
pprint(arr)
pprint(arr.swapaxes(1, 2))
print("*" * 40) 
