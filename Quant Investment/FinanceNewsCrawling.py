# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:47:40 2025

@author: Administrator
"""
### 금융속보 크롤링###

import requests as rq
from bs4 import BeautifulSoup

import pandas as pd

url = 'https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258'
data = rq.get(url)      #get 함수를 이용해 페이지의 내용을 받아 온다.

#BeautifulSoup 함수를 통해 html 정보를 BeautifulSoup 객체로 만든다
html = BeautifulSoup(data.content, 'html.parser')

#select 함수를 통해 원하는 태그로 접근한다.
html_select = html.select('dl > dd.articleSubject > a')

#제목은 title 속성에 위치한다.
#print(html_select[0]['title'])

#print(html_select[0:3])

#for문으로 묶어 한 번에 제목들을 추출한다.
#print([i['title'] for i in html_select])


###국가별 시가 총액 ###

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_stock_market_capitalization'
tbl = pd.read_html(url)

print(tbl[0].head())