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

# 6.3 与Web API交互
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
print(resp)

data = resp.json()
print(data[0]['title'])

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
pprint(issues)