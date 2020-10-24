# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:44:55 2020

@author: Cliff
"""

# Dat-129  Python2 Programming
# Assignment API Module using NASA API
# Due 09-30-2020
# Clifford B. Rohal

# NeoWs (Near Earth Object Web Service) is a RESTful web service for near
# earth Asteroid information. With NeoWs a user can: search for Asteroids based
# on their closest approach date to Earth, lookup a specific Asteroid with its
# NASA JPL small body id, as well as browse the overall data-set.


import requests #third party library used to get data from the internet
import pprint

api_key = "EOkBPMTDwuSeAtb58CtXp3fw1cxPrqawvwy10RQ6"
base_url = "https://api.nasa.gov/neo/rest/v1/feed"
start_date = "2020-10-07"
end_date = "2020-10-07"

parameters = {"api_key":api_key, "start_date": start_date, "end_date": end_date}

response = requests.get(base_url, params=parameters)


print("="*88)
pprint.pprint(response.json())
print("-"*88)
print(response.url)
