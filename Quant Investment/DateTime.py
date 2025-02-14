# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:26:16 2025

@author: Administrator
"""

###시계열 데이터 : 시간을 기준으로 측정된 자료

import seaborn as sns
import pandas as pd

df = sns.load_dataset('taxis')
#print(df.head())

##pickup과 dropoff 열을 살펴보면 시계열 형태처럼 보인다

"""
               pickup             dropoff  ...  pickup_borough  dropoff_borough
0 2019-03-23 20:21:09 2019-03-23 20:27:24  ...       Manhattan        Manhattan
1 2019-03-04 16:11:55 2019-03-04 16:19:00  ...       Manhattan        Manhattan
2 2019-03-27 17:53:01 2019-03-27 18:00:25  ...       Manhattan        Manhattan
3 2019-03-10 01:23:59 2019-03-10 01:49:51  ...       Manhattan        Manhattan
4 2019-03-30 13:27:42 2019-03-30 13:37:14  ...       Manhattan        Manhattan
"""



##to_datetime() 메서드를 통해 문자열을 datetime 객체로 변환할 수 있다
df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])

#print(df.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 6433 entries, 0 to 6432
Data columns (total 14 columns):
 #   Column           Non-Null Count  Dtype         
---  ------           --------------  -----         
 0   pickup           6433 non-null   datetime64[ns]
 1   dropoff          6433 non-null   datetime64[ns]
 2   passengers       6433 non-null   int64         
 3   distance         6433 non-null   float64       
 4   fare             6433 non-null   float64       
 5   tip              6433 non-null   float64       
 6   tolls            6433 non-null   float64       
 7   total            6433 non-null   float64       
 8   color            6433 non-null   object        
 9   payment          6389 non-null   object        
 10  pickup_zone      6407 non-null   object        
 11  dropoff_zone     6388 non-null   object        
 12  pickup_borough   6407 non-null   object        
 13  dropoff_borough  6388 non-null   object        
dtypes: datetime64[ns](2), float64(5), int64(1), object(6)
memory usage: 703.7+ KB
"""
##pickup열에서 연도에 해당하는 정보만 추출
#print(df['pickup'][0].year) #2019


df['year'] = df['pickup'].dt.year
df['month'] = df['pickup'].dt.month
df['day'] = df['pickup'].dt.day
print(df[['pickup','year', 'month', 'day']].head())