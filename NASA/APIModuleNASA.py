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
# Retrieve a list of Asteroids based on their closest approach date to Earth.

import requests #third party library used to get data from the internet
import pprint
import json as json

clear = "\n" * 100 # to clear the Ippython console when printed

#def get_data(start_date, end_date):
# defining the API key and the location of the data
api_key = "EOkBPMTDwuSeAtb58CtXp3fw1cxPrqawvwy10RQ6"
base_url = "https://api.nasa.gov/neo/rest/v1/feed"

#Start date and end date.  Make this an input from a user interface
#def input_date():
print(clear)
start_date = input("Input start date in YYYY-MM-DD format: ")
end_date = start_date

# api_key=API_KEY start_date=START_DATE end_date=END_DATE
parameters = {"api_key":api_key, "start_date": start_date, "end_date": end_date}
response = requests.get(base_url, params=parameters)

# collecting all data into json
neows_data = json.loads(response.text)
neos = neows_data['near_earth_objects']
neos_date = neos[start_date]

#-----------------------------------------------------------------------------
#return start_date, end_date
def print_key_info():
    print(\
    f"""
    Keys for the direct response data (neows_data):
    {neows_data.keys()}   
    
    Key for the NEOs data (neos):
    {neos.keys()}
    
    No "keys" property, has "iter" method, neo date (neos_date) declared iterable:
    {dir(neos_date)}
    
    Source:
    {base_url}
    
    API Key:
    {api_key}
    """   
    )

#-----------------------------------------------------------------------------
# drilling down to extract the desired data.
# Note: some data is stored in a dictionary and others are iterable lists.
def user_data():
    neo_cnt = 0
    for neo in neos_date:
        magnitude = neo['absolute_magnitude_h']
        # close approach data
        close_data = neo['close_approach_data']
        for close in close_data: #close_approach_data is a list and needs iterated
            close_date = close['close_approach_date_full']
            miss_dist = close['miss_distance']
            # dictionary of the missed distances, no iterator required
            dist_kilo = float(miss_dist['kilometers'])
            dist_lunar = float(miss_dist['lunar'])
            dist_miles = float(miss_dist['miles'])
            
            # dictionary of the relative velocity, no iterator required
            rel_vel = close['relative_velocity']
            vel_kilo_hour = float(rel_vel['kilometers_per_hour'])
            vel_kilo_sec = float(rel_vel['kilometers_per_second'])
            vel_mph = float(rel_vel['miles_per_hour'])
        # estimated diameter of near earth object (NEO)
        estimated_dia = neo['estimated_diameter']
        for diameter in estimated_dia: # list data iterator required
            diameter = estimated_dia['feet']
            for ft in diameter: # list data iterator required
                dia_feet_max = diameter['estimated_diameter_max']
                dia_feet_min = diameter['estimated_diameter_min']
        diameter = neo['estimated_diameter'] 
        neo_id = neo['id']
        hazardous = neo['is_potentially_hazardous_asteroid']
        name = neo['name']
        nasa_url = neo['nasa_jpl_url']
        neo_cnt += 1
        print(\
    f"""NEO close approach: {close_date}
    Magnitude: {magnitude}
    Identifier: {neo_id}
    Name: {name}
    Hazardous: {hazardous}
    Distance: {dist_kilo:,.2f} km
    Distance: {dist_lunar:,.2f} LD
    Distance: {dist_miles:,.2f} mi
    Velocity: {vel_kilo_hour:,.2f} kph
    Velocity: {vel_kilo_sec:,.2f} kps
    Velocity: {vel_mph:,.2f} mph
    Max Diameter: {dia_feet_max:,.2f} ft
    Min Diameter: {dia_feet_min:,.2f} ft
    NASA Link: {nasa_url}
    """
    ) 
    return neo_cnt

#-----------------------------------------------------------------------------
# print in json format
def print_json_data():
    pprint.pprint(neos_date)
    print("")

#=============================================================================    
def main():
    select = ""
    while select != 'x':
        print(\
f""""k" for key list
"j" for json format
"u" for user format """
)
        select = input('Or press "x" to exit: ')
        if select == 'k':
            print(clear)
            print_key_info()
        else:
            if select == 'u':
                print(clear)
                neo_cnt = user_data()
                print('The total near earth objects for', start_date,'is',neo_cnt)
                print('')
            else:
                if select == 'j':
                    print(clear)
                    print_json_data()
#=============================================================================    

main()
        