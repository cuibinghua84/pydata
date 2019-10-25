# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.2-二进制格式.py
@time: 2019/10/22 11:23
"""

import pandas as pd
from pprint import pprint

path = 'D:/data/pydata_book2/examples/ex1.csv'
# frame = pd.read_csv(path)
# pprint(frame)

# 写入二进制文件
# frame.to_pickle('D:/data/pydata_book2/examples/frame_pickle')

# 读取二进制文件
pprint(pd.read_pickle('D:/data/pydata_book2/examples/frame_pickle'))

# 6.2.1 使用HDF5格式

# 6.2.2 读取Microsoft Excel文件
