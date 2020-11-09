"""
Created on Sun Nov  8 12:25:13 2020
@author: Cliff
"""
# Dat-129  Python2 Programming
# Assignment NASA API to a sq Database
# Due 11-11-2020
# Clifford B. Rohal
# NeoWs (Near Earth Object Web Service) is a RESTful web service for near
# earth Asteroid information and to store in a database.

import pprint
import APIModuleNASADB
import sqlite3

with sqlite3.connect('NEO_DB.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists NEO_Table(Date text, Magnitude real,
        Identifier integer, Hazardous text, DistanceKM real, DistanceLD real,
        DistanceMI real, VelocityKPH real,VelocityKPS real,VelocityMPH real,
        MaxDiaFT real, MinDiaFT real, NASALink text)
    ''')    
    NEO_Data = APIModuleNASADB.main()
    for segment in NEO_Data:
        cursor.execute('''
        INSERT INTO NEO_Table (Date, Magnitude, Identifier,
        Hazardous, DistanceKM, DistanceLD, DistanceMI, 
        VelocityKPH,VelocityKPS,VelocityMPH, MaxDiaFT,
        MinDiaFT, NASALink)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);
    ''',segment)
# SELECT Orders the computer to include or select each content from the
# database name(table ), (*) means all, FROM refers from where to select the data.
    cursor.execute('select * from NEO_Table')
    pprint.pprint(cursor.fetchall()) # get all data row by row
