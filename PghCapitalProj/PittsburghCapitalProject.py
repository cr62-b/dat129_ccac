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
#mport pandas as pd
with open("cgcapitalprojects_img.geojson", "r") as file:
    cap_proj = json.load(file)

print(cap_proj.keys()) #print the keys to the dictonary in the geojson file 
print("-"*88) # prints - 88 times


features = cap_proj["features"] #feature variable = features dictonary

total_money = 0
no_budget = 0

for unit in features:
    #drilling down in the features dictionary the budgeted amount
    budget_amount = unit['properties']['budgeted_amount']
    try:
        total_money += budget_amount
    except TypeError:
        no_budget += 1    #counting the entries without a budget amount

i = 0
while i <1:
    pprint(features[i])
    print("-"*88) # prints - 88 times
    myfeatures = str(features[i])
    myfile = open("CapitalProj.txt","w")
    myfile.write(myfeatures + "\n")
    i += 1

#convert to a currency
average = "${:,.2f}".format((total_money / len(features)-no_budget))
total_money = "${:,.2f}".format(total_money)

#Write data to file
myfile.write(average + "\n")
myfile.write(total_money + "\n")

print("Budget Total:", total_money)
print("Average Budget:", average)

myfile.close


