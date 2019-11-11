#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
# 通用函数：快速的逐元素数组函数
# 也称ufunc，是一种在ndarray数据中进行逐元素操作的函数
# 一元通用函数
arr = np.arange(10)
arr
np.sqrt(arr)
np.exp(arr)

# 二元通用函数
x = np.random.randn(8)
y = np.random.randn(8)
x
y
# maximun
np.maximum(x, y)

# modf：返回一个浮点值数组的小数部分和整数部分
arr = np.random.randn(7) * 5
arr
remainder, whole_part = np.modf(arr)
remainder
whole_part

# 通用函数接收一个可选参数out，允许对数组按位操作
# arr
# np.sqrt(arr)
# np.sqrt(arr, arr)
# arr

"""
一元通用函数
abs、fabs：逐元素计算整数、浮点数或复数的绝对值
sqrt：计算每个元素的平方根
square：计算每个元素的平方

二元通用函数
add：将数组的对应元素相加
subtract：在第二个数字中，将第一个数字中包含的元素去除
multiply：将数组的对应元素相乘
divide、floor_divide：除或整除（放弃余数）
power：将第二个数组的元素，作为第一给数组对应元素的幂次方
maximun，fmax：逐个元素计算最大值，fmax忽略NaN
minimum，fmin：逐个元素计算最小值，fmin忽略NaN
mod：按元素的求模计算
copysign：将第一个数组的符号改为第二个数组的符号值
greater，greater_equal，less：进行逐个元素的比较，返回布尔值数组（与数学操作符> >= < <= == !=）
less_equal，equal，not_equal
logical_and， logical_or：进行逐个元素的逻辑操作（与逻辑操作符& | ^效果一致）
logical_xor
"""


# In[ ]:




