import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('tamashebi.csv','w',newline='',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['title'])
num = 1
for i in range(5):
    url = f'https://www.sonsaur.com/?query-69301c7f-page={num}'
    response = requests.get(url)
    soup = BeautifulSoup( response.text, 'html.parser' )
    dv = soup.find( 'div', {'class': 'gb-grid-wrapper gb-grid-wrapper-604087d2 gb-query-loop-wrapper'} )
    titles = [elem.text.replace('\n','') for elem in dv.find_all( 'div', {'class': 'gb-container gb-container-05370b11'} )]
    for i in titles:
        writer.writerow([i])
    num+=1
    sleep(randint(10,15))