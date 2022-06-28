#from : https://stackhoarder.com/2019/08/18/python%EB%B6%80%ED%84%B0-web-scraping-%EA%B9%8C%EC%A7%80-%EC%B5%9C%EB%8B%A8-%EC%8B%9C%EA%B0%84%EC%97%90-%EC%9D%B5%ED%98%80%EB%B3%B4%EC%9E%90/

import  requests
from bs4 import BeautifulSoup
from time import sleep

r = requests.get('https://twitter.com/A_Dark_night_')
html = r.text

soup = BeautifulSoup(html, 'html.parser')
title = soup.select('title')
print(title)
#print(html)