# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#190p 8.2 크롤링 예제

import requests as rq
from bs4 import BeautifulSoup


#url에 해당 주소를 입력한다.
url = 'https://quotes.toscrape.com/'

#get()함수를 이용해 해당 페이지의 내용을 받았다.
quote = rq.get(url)

#print(quote)
#print(quote.content[:1000]) 
                    


url = 'https://quotes.toscrape.com/'
quote = rq.get(url)
quote_html = BeautifulSoup(quote.content, 'html.parser')
#print(quote_html.head())
"""
[<meta charset="utf-8"/>, <title>Quotes to Scrape</title>,
 <link href="/static/bootstrap.min.css" rel="stylesheet"/>, 
 <link href="/static/main.css" rel="stylesheet"/>]
"""


quote_div = quote_html.find_all('div', class_='quote')
#print(quote_div[0])
"""
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
<span>by <small class="author" itemprop="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags">
            Tags:
            <meta class="keywords" content="change,deep-thoughts,thinking,world" itemprop="keywords"/>
<a class="tag" href="/tag/change/page/1/">change</a>
<a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
<a class="tag" href="/tag/thinking/page/1/">thinking</a>
<a class="tag" href="/tag/world/page/1/">world</a>
</div>
</div>
"""


quote_span = quote_div[0].find_all('span', class_='text')
#print(quote_span)
"""
[<span class="text" itemprop="text">“The world as we have created it is
 a process of our thinking. It cannot be changed without changing our
 thinking.”</span>]
"""

#print(quote_span[0].text)
"""
“The world as we have created it is a process of our thinking.
It cannot be changed without changing our thinking.”
"""

quote_div = quote_html.find_all('div', class_ = 'quote')

#결과물 마지막에 .text를 입력하면 텍스트 데이터만을 출력할 수 있다.
#for문 중에서 리스트 내포 형태를 이용하여 명언에 해당하는 부분을 한번에
#추출한다.
print([i.find_all('span', class_ = 'text')[0].text for i in quote_div])

###여기까지 8.2.1.1