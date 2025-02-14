# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:56:12 2025

@author: Administrator
"""

"""
import pandas as pd

#키 : a,b,c  값 : 1,2,3인 딕셔너리 생성
dict_data = {'a' : 1, 'b' : 2,'c' : 3,}
series = pd.Series(dict_data)   #Series 함수에 입력하면 series객체로 변환

print(series)
"""

#딕셔너리가 아닌 리스트를 통해 시리즈 만들기
"""
import pandas as pd

#리스트를 통해 시리즈를 만들 경우,
#인덱스는 정수형 위치 인덱스(0,1,2...)가 자동 지정됨
list_data = ['x', 'y', 'x']     #[] : 리스트 형식
series_2 = pd.Series(list_data)
series_3 = pd.Series(list_data, index=['index3','index4','index5'])

print(series_3)
"""

### 키 : 국가, 값 : 수도로 이루어진 시리즈 만들기###

"""
import pandas as pd

capital = pd.Series({'Korea' : 'Seoul',
                     'Japan' : 'Tokyo',
                     'China' : 'Beijing',
                     'India' : 'New Delhi',
                     'Taiwan' : 'Taipei',
                     'Singapore' : 'Singapore'
                     })

#위치 인덱스를 리스트 형태로 입력   # 0번째와 3번째 원소 출력
# https://mcc96.tistory.com/57 : iloc 설명
#print(capital.iloc[[0, 3]]) 

# 0:3 -> 0이상 3미만을 뜻한다
#print(capital.iloc[0:3])
#print(capital['Korea'])     #한국에 해당하는 데이터 선택

#print(capital)
"""


###시리즈 사칙연산###
import pandas as pd

series_1 = pd.Series([7,8,9])
series_2 = pd.Series([10,11,12])

#0번째,1번째, 2번째 연산 결과 출력됨 
print(series_1 + series_2)