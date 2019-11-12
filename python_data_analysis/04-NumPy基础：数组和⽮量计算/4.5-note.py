# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.5-note.py
@time: 2019/11/12 10:56
"""

import numpy as np
from pprint import pprint
from numpy.linalg import inv, qr

# 线性代数
# 矩阵操作
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
pprint(x)
pprint(y)
pprint(x.dot(y))

pprint(np.dot(x, y))
pprint(np.dot(x, np.ones(3)))

pprint(x @ np.ones(3))

print("*" * 40)
X = np.random.randn(5, 5)
mat = X.T.dot(X)
pprint(inv(mat))

pprint(mat.dot(inv(mat)))

q, r = qr(mat)
pprint(r)
"""
常用numpy.linalg函数
diag：将一个方阵的对角（或非对角）元素作为一维数组返回，或者将一维数组转换成一个方阵，并且在非对角线上有零点
dot：矩阵点乘
trace：计算对角元素和
det：计算矩阵的行列式
eig：计算方阵的特征值和特征向量
inv：计算方阵的逆矩阵
pinv：计算矩阵的Moore-Penrose伪逆
qr：计算QR分解
svd：计算奇异值分解（SVD）
solve：求解x的线性系统Ax=b，其中A是方阵
lstsq：计算Ax=b的最小二乘解
"""

