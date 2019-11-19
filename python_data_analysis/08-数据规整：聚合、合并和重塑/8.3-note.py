# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 8.3-note.py
@time: 2019/11/18 11:42
"""

import numpy as np
import pandas as pd
from pandas import DataFrame, Series
from pprint import pprint


def fs():
    print("*" * 40)


# 8.3 重塑和透视
# 8.3.1 使用多层索引进行重塑
data = pd.DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)
fs()
result = data.stack()
print(result)

fs()
print(result.unstack())

fs()
print(result.unstack(0))

fs()
print(result.unstack('state'))



# 8.3.2 将“长”透视为“宽”

# 8.3.3 将“宽”透视为“长”
