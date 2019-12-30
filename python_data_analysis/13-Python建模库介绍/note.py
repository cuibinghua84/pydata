# -*- coding: utf-8 -*-
"""
@author: 东风
@file: note.py
@time: 2019/12/20 9:50
"""

import pandas as pd
import numpy as np

# 13.1 pandas与建模代码的结合
data = pd.DataFrame({'x0': [1, 2, 3, 4, 5],
                     'x1': [0.01, -0.01, 0.25, -4.1, 0],
                     'y': [-1.5, 0., 3.6, 1.3, -2.]})
print(data)
print(data.columns)
print(data.values)
# 13.2 使用Patsy创建模型描述

# 13.3 statsmodels介绍

# 13.4 sckit-learn介绍

# 13.5 继续你的教育
