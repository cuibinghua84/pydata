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
# 8 生成数组最简单的方式就是使用array函数

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)








