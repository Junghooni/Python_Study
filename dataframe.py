# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:35:07 2025

@author: Administrator
"""

### DataFrame : 흔히 엑셀에서 사용하는 행과 열로 이루어진 표 형태


import pandas as pd
"""
dict_data = {'col1' : [1,2,3], 'col2' : [10,11,12], 'col3' : [20,21,22]}
df = pd.DataFrame(dict_data)

print(df)
"""

#리스트 형태로 데이터 프레임을 만들면 각각의 리스트가 그대로 행의 형태로 출력됨
#반면 행 인덱스와 열 이름은 기본값인 위치 인덱스가 부여됨

df2 = pd.DataFrame(([[23.2,231.9,555],[67,43,65],[89,54,87]]))

print(df2)

"""
      0      1    2
0  23.2  231.9  555
1  67.0   43.0   65
2  89.0   54.0   87
"""


#행 인덱스와 열 이름을 직접 지정하고자 할 경우, 리스트 형태로 입력한다.
df3 = pd.DataFrame([[23.2,231.9,555],[67,43,65],[89,54,87]],
                   index=['index1', 'index2', 'index3'],
                   columns=['col1', 'col2', 'col3'])

print(df3)

"""
        col1   col2  col3
index1  23.2  231.9   555
index1  67.0   43.0    65
index2  89.0   54.0    87
"""

#데이터 프레임의 행과 열 삭제
#행 삭제 시 axis=0, 열 삭제 시 axis=1을 입력한다
#inplace=True 옵션은 원본 데이터가 변경됨
df3.drop('index2', axis=0, inplace=True)
df3.drop('col2', axis=1, inplace=True)

print(df3)

"""
        col1  col3
index1  23.2   555
index3  89.0    87
"""