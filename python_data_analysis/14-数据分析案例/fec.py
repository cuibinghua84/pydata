li# -*- coding: utf-8 -*-
"""
@author: 东风
@file: fec.py
@time: 2019/11/29 17:40
"""

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from pprint import pprint

path = 'D:/data/pydata_book2/datasets/fec/P00000001-ALL.csv'
fec = pd.read_csv(path, low_memory=False)

# 信息加载
pprint(fec.info())

# 打印一条样本记录
# print(fec.iloc[123456])

# 使用unique获得所有不同的政治候选人名单
# unique_cands = fec.cand_nm.unique()
# pprint(unique_cands)
# pprint(unique_cands[2])

parties = {
    'Bachmann, Michelle': 'Republican',
    'Cain, Herman': 'Republican',
    'Gingrich, Newt': 'Republican',
    'Huntsman, Jon': 'Republican',
    'Johnson, Gary Earl': 'Republican',
    'McCotter, Thaddeus G': 'Republican',
    'Obama, Barack': 'Democrat',
    'Paul, Ron': 'Republican',
    'Pawlenty, Timothy': 'Republican',
    'Perry, Rick': 'Republican',
    "Roemer, Charles E. 'Buddy' III": 'Republican',
    'Romney, Mitt': 'Republican',
    'Santorum, Rick': 'Republican'
}

# print(fec.cand_nm[123456: 123461])
# print(fec.cand_nm[123456: 123461].map(parties))
