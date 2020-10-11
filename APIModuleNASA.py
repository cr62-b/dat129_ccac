# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:44:55 2020

@author: Cliff
"""

"""
Dat-129  Python2 Programming
Assignment API Module using NASA API
Due 09-30-2020
Clifford B. Rohal
"""

import requests #third party library used to get data from the internet
import pprint

api_key = "EOkBPMTDwuSeAtb58CtXp3fw1cxPrqawvwy10RQ6"
base_url = "https://api.nasa.gov/neo/rest/v1/feed"
start_date = "2020-10-07"
end_date = "2020-10-08"

parameters = {"api_key":api_key, "start_date": start_date, "end_date": end_date}

response = requests.get(base_url, params=parameters)


print(response)
print(response.text)
print(response.json())
pprint.pprint(response.json())
print(response.url)
