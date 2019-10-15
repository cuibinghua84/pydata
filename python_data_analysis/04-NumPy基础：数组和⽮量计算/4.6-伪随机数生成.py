# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.6-伪随机数生成.py
@time: 2019/10/12 17:39
"""

import numpy as np
from pprint import pprint

# normal获得4*4的正态分布样本数据
samples = np.random.normal(size=(4, 4))
pprint(samples)


