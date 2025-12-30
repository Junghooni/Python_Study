import pandas as pd


# 시리지 함수는 1차원 배열이다

series_1 = pd.Series([50,77,80])
series_2 = pd.Series([23,78,90])

# 시리즈 함수로 사칙연산 하기
print(series_1 + series_2)
print(series_1 * series_2)
print(series_1 * 2)
print(series_2 * 3)

"""
0     73
1    155
2    170
dtype: int64

0    1150
1    6006
2    7200
dtype: int64

0    100
1    154
2    160
dtype: int64
0     69
1    234
2    270
dtype: int64

"""
