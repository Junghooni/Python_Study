import pandas as pd
import selenium.webdriver

#pandas의 Dataframe()함수는 데이터프레임을 만드는 역할을 한다.
df = pd.DataFrame({'x' : [1,2,3]})

#print(df)

# 딕셔너리는 중괄호를 사용한다.
dict_data = {'a':11,'b':22,'c':33}
series = pd.Series(dict_data)

#print(series.index)
## Index(['a', 'b', 'c'], dtype='object')

#print(series.values)
## [11 22 33]

#리스트를 만들시 대괄호를 사용한다.
list_data = ['x','y','z']
series_2= pd.Series(list_data)
#print(series_2)
"""
0    x
1    y
2    z
dtype: object

series_2의 출력값을 보면
리스트를 통해 시리즈를 만들 경우, 인덱스는 정수형 위치 인데스가 자동으로
지정된다.
"""

series_3 = pd.Series(list_data, index=['no1','no2','no3'])
#print(series_3)

"""
no1    x
no2    y
no3    z
dtype: object

리스트를 통해 시리즈를 만든후 , index 옵션에
인덱스 이름을 직접 입력하여 인덱스를 생성 할 수 있다.
"""

### 3.1.2 원소 선택하기
# 키로는 국가명, 값으로는 수도로 이루어진 시리즈를 만듬
capital = pd.Series({'korea':'seoul',
                     'japan':'tokyo',
                     'india':'new delhi',
                     'taiwan':'taipei',
                     'singapore':'singapore'})
#print(capital)
"""
korea            seoul
japan            tokyo
india        new delhi
taiwan          taipei
singapore    singapore
dtype: object
"""

# 이중에 한국에 해당하는 데이터를 선택하는 법은 다음과 같다
#print(capital['korea'])
# seoul

"""
시리즈의 특징 중 하나는 한번에 여러개의 인덱스를 입력할 수 있다
값을 찾고싶은 인덱스를 리스트 형태로 입력하면 이에 해당하는 모든 원소가
선택된다.
"""
print(capital[['korea','taiwan','india']])
"""
korea         seoul
taiwan       taipei
india     new delhi
dtype: object
"""
