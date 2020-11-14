# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:36:31 2020

@author: Cliff
"""

import requests
# Import beautiful soup module
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/country/us/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
ownername = soup.find('table', id='usa_table_countries_today')

outfile = open('covid_usa.txt', 'w')

print(ownername.text)

rows = ownername.findAll('tr')
for r in rows:
    tds = r.findAll('td')
    for td in tds:
        print(td.text)
        outfile.write(td.text)
   
outfile.close()
