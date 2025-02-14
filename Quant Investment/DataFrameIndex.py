# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:00:18 2025

@author: Administrator
"""

#데이터 요약 정보 및 통계값

import seaborn as sns

"""
df = sns.load_dataset('titanic')    #타이타닉 데이터 셋

print(df.head())        #맨 위 5개 행의 데이터를 볼 수 있다.
print(df.tail())        #맨 아래 5개 행의 데이터를 볼 수 있다.
#데이터 프레임의 크기, 행과 열의개수를 튜플 형태로 반환함 / 행891개, 열 15개
print(df.shape)
"""

#데이터 프레임의 인덱스(행) 다루기
#인덱스를 변경하거나 정렬하고, 재설정하는 법

df = sns.load_dataset('mpg')
#print(df.head())    #인덱스를 보면 0,1,2 위치 인덱스 형태로 출력된다

##자동차 이름인 name으로 인덱스를 설정한다
df.set_index('name', inplace=True)
#print(df.head())
"""
mpg  cylinders  displacement  ...  model_year  origin                       name
0  18.0          8         307.0  ...          70     usa  chevrolet chevelle malibu
1  15.0          8         350.0  ...          70     usa          buick skylark 320
2  18.0          8         318.0  ...          70     usa         plymouth satellite
3  16.0          8         304.0  ...          70     usa              amc rebel sst
4  17.0          8         302.0  ...          70     usa                ford torino
"""

##sort_index() 메서드를 통해 인덱스가 알파벳 순서대로 정렬됨
#df.sort_index(inplace=True)
#print(df.head())

"""
                          mpg  cylinders  ...  model_year  origin
name                                      ...                    
amc ambassador brougham  13.0          8  ...          73     usa
amc ambassador dpl       15.0          8  ...          70     usa
amc ambassador sst       17.0          8  ...          72     usa
amc concord              24.3          4  ...          80     usa
amc concord              19.4          6  ...          78     usa
"""

##내림차순으로 정렬하고 싶다면 ascending=False를 입력한다.
#df.sort_index(inplace=True, ascending=False)
#print(df.head())

"""
                       mpg  cylinders  ...  model_year  origin
name                                   ...                    
vw rabbit custom      31.9          4  ...          79  europe
vw rabbit c (diesel)  44.3          4  ...          80  europe
vw rabbit             29.0          4  ...          76  europe
vw rabbit             41.5          4  ...          80  europe
vw pickup             44.0          4  ...          82  europe
"""


#인덱스 재설정은 reset_index() 메서드르르 사용한다.
#인덱스가 다시 [0,1,2...]의 위치인덱스로 변경되고, 기존에 존재하던
#인덱스는 'name'열로 옮겨진다
df.reset_index(inplace=True)
print(df.head())
"""
                        name   mpg  cylinders  ...  acceleration  model_year  origin
0  chevrolet chevelle malibu  18.0          8  ...          12.0          70     usa
1          buick skylark 320  15.0          8  ...          11.5          70     usa
2         plymouth satellite  18.0          8  ...          11.0          70     usa
3              amc rebel sst  16.0          8  ...          12.0          70     usa
4                ford torino  17.0          8  ...          10.5          70     usa

[5 rows x 9 columns]
"""