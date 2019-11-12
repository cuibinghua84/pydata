# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.6-note.py
@time: 2019/11/12 10:56
"""

import numpy as np
from pprint import pprint
from numpy.linalg import inv, qr

# 伪随机数生成
# 4x4的正态分布样本数据
samples = np.random.normal(size=(4, 4))
pprint(samples)


"""
# numpy.random在生成大型样本时比存Python的方式快了一个数量级
from random import normalvariate
N = 1000000
%timeit samples = [normalvariate(0, 1) for _ in range(N)]
1.4 s ± 21.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
import numpy as np
%timeit np.random.normal(size=N)
40.7 ms ± 2.15 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

# 还可以通过np.random.seed更改NumPy的随机种子数
"""

rng = np.random.RandomState(1234)
pprint(rng.randn(10))

"""
numpy.random中部分函数列表
seed：向随机数生成器传递随机状态种子
permutation：返回一个序列的随机排列，或者返回一个乱序的整数范围序列
shuffle：随机排列一个序列
rand：从均匀分布中抽取样本
randint：根据指定的由低到高的范围抽取随机整数
randn：从均值0方差1的正态分布中抽取样本
binomial：从二项分布中抽取样本
normal：从正态分布中抽取样本（高斯）
beta：从beta分布中抽取样本
chisquare：从卡方分布中抽取样本
"""