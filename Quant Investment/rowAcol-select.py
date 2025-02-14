# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:04:26 2025

@author: Administrator
"""

#열과 행 선택하기

import pandas as pd

dict_data = {'col1' : [1,2,3,4], 'col2' : [5,6,7,8],
             'col3' : [9,10,11,12], 'col4' : [13,14,15,16]}
df = pd.DataFrame(dict_data, index=['index1', 'index2', 'index3', 'index4'])

"""
#df['열 이름']
#df.열 이름

index1    5
index2    6
index3    7
index4    8
Name: col2, dtype: int64
"""

#데이터 프레임 형태로 반환
"""
        col2
index1     5
index2     6
index3     7
index4     8
"""
print(df[['col2']])