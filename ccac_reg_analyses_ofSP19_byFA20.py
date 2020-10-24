# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:34:30 2020

@author: Cliff
"""


# Pandas introduction using a flat file of all registrations for 
# courses at CCAC during spring 2019:
# What programs are home to students whose mid-term grades are, on
# average, lower than other?  Are mid-term grades good predictors of final
# grades?
# How likely

import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt

# Special magic function for enabling pyplot charts in jupyter
#%matplotlib inline


# Read in the CSV, it's pretty to start with, so thatit's easy
stud_records = pd.read_csv("19sp_gradestud_only.csv")
recs = stud_records

cyber = recs.loc[lambda recs: recs['LocationType'].isin(['Online'])]
onsite = recs.loc[lambda recs: recs['LocationType'].isin(['On-site'])]

plt.plot(cyber['CreditsAtStartofTerm'])

print("-"*88) # prints - 88 times
print(stud_records.iloc[56400:56408])
print("-"*88) # prints - 88 times
print(stud_records.loc[56408])
print("-"*88) # prints - 88 times
print(stud_records)
print("-"*88) # prints - 88 times
print(cyber)

print("-"*88) # prints - 88 times
print('Onsite: ', len(onsite))
print('Cyber:  ', len(cyber))

