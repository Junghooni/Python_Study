#194p 8.2.1.2 select 함수를 이용한 크롤링

import requests as rq
from bs4 import BeautifulSoup


#url에 해당 주소를 입력한다.
url = 'https://quotes.toscrape.com/'

#get()함수를 이용해 해당 페이지의 내용을 받았다.
quote = rq.get(url)
                 
url = 'https://quotes.toscrape.com/'
quote = rq.get(url)
quote_html = BeautifulSoup(quote.content, 'html.parser')
quote_div = quote_html.find_all('div', class_='quote')
quote_span = quote_div[0].find_all('span', class_='text')
quote_div = quote_html.find_all('div', class_ = 'quote')

quote_text = quote_html.select('div.quote > span.text')
#print(quote_text)
"""
[<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>,
<span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>, <span class="text" itemprop="text">
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”</span>, <span class="text" itemprop="text">
“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>, <span class="text" itemprop="text">“Imperfection is beauty, madness is
genius and it's better to be absolutely ridiculous than absolutely boring.”</span>, <span class="text" itemprop="text">“Try not to become a man of success. Rather become a man of value.”</span>,
<span class="text" itemprop="text">“It is better to be hated for what you are than to be loved for what you are not.”</span>, <span class="text" itemprop="text">“I have not failed.
I've just found 10,000 ways that won't work.”</span>, <span class="text" itemprop="text">“A woman is like a tea bag; you never know how strong it is until it's in hot water.”</span>,
<span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>]
"""

#[class가 quote인 div 태그] 중에서 [class가 text인 span 태그]를 찾는다.
quote_text_list = [i.text for i in quote_text]
print(quote_text_list)
"""
['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', '“It is our choices, Harry, that show what we truly are,
far more than our abilities.”', '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', '“The person,
be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous
than absolutely boring.”", '“Try not to become a man of success. Rather become a man of value.”', '“It is better to be hated for what you are than to be loved for what you are not.”',
"“I have not failed. I've just found 10,000 ways that won't work.”", "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", '“A day without sunshine is like, you know, night.”']
"""
