# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:26:09 2019

@author: p_bhcui
"""
import numpy as np
import pandas as pd
from pprint import pprint
import sys
import csv
import json


def fs():
    print("*" * 40)


# 6.2 二进制格式
# 6.2.1 使用HDF5格式

# 6.2.2 读取Microsoft Excel文件
xlsx = pd.ExcelFile('examples/ex1.xlsx')
pprint(pd.read_excel(xlsx, 'Sheet1'))

frame = pd.read_excel('examples/ex1.xlsx', 'Sheet1')
pprint(frame)

writer = pd.ExcelWriter('examples/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()

frame.to_excel('examples/ex3.xlsx')
