# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:17:23 2025

@author: Administrator
"""

###데이터 불러오기

import pandas as pd

data_csv = pd.read_csv(
    'https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv')

print(data_csv)
print(data_csv.to_csv('data.csv'))