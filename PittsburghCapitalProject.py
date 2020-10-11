# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:33:05 2020

@author: Cliff
"""

"""
Dat-129  Python2 Programming
Assignment Pittsburgh Capital Project
Due 09-16-2020
Clifford B. Rohal

Session on JSON
Shows the basic usage of the json module and then inject data in JSON format
for processing and exporting transportable information.
"""
import json
from pprint import pprint

with open("cgcapitalprojects_img.geojson", "r") as file:
    cap_proj = json.load(file)

print(cap_proj.keys())

features = cap_proj["features"]

total_money = 0

no_budget = 0

for unit in features:
    budget_amount = unit['properties']['budgeted_amount']
    try:
        total_money += budget_amount
    except TypeError:
        no_budget += 1    

average = total_money / len(features)-no_budget

pprint(total_money)
pprint(average)


