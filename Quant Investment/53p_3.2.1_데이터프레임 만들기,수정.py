import pandas as pd


# 데이터프레임 함수는 2차원 배열이다

dict_data = {'col1':[12,23,34], 'col2':[45,56,67], 'col3':[78,89,90]}
df = pd.DataFrame(dict_data)

#print(df)
"""
   col1  col2  col3
0    12    45    78
1    23    56    89
2    34    67    90
"""

df3 = pd.DataFrame([[99,87,76],[54,32,66],[21,43,26]],
                   index=['row1','row2','row3'],
                   columns=['col1','col2','col3'])
df3.rename(index={'row1':'행1'}, inplace=True)
df3.rename(columns={'col1':'열1'}, inplace=True)

print(df3)
"""
      col  col2  col3
row1   99    87    76
row2   54    32    66
row3   21    43    26

리스트를 통해 데이터 프레임을 만들 수 도 있다.
Dataframe() 함수 내부에 리스트 형태인 [[99,87,76],[54,32,66],[21,43,26]
를 다시 리스트에 넣어 중첩 형태로 입력하면, 각각의 리스트가 그대로 행의 형태로
입력된다. 반면 행 인덱스와 열 이름은 기본값인 위치 인덱스가 부여된다.

      열1  col2  col3
행1    99    87    76
row2  54    32    66
row3  21    43    26

df3.rename(index={'row1':'행1'}, inplace=True)
df3.rename(columns={'col1':'열1'}, inplace=True)
상기의 rename으로 행 인덱스나 열 이름 중 원하는 부분만을 선택해
변경할 수도 있다.

"""
