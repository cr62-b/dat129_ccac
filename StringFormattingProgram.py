# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:41:07 2020

@author: Cliff
"""

"""
Dat-129  Python2 Programming
Assignment String Formatting Program
Due 09-09-2020
Clifford B. Rohal
"""

#Working from the Testing branch

FileName = "Names.txt"
DataFile = open(FileName, 'r')
List = DataFile.read()

#Output the list in file: Names
def DataList():
    print("--------------------------------")
    print("Names in file Names.txt:")
    print(List)

#Modify the data by adding "Good eveing dr."
def GoodEvening():
    LastName = "F"
    for line in List:
        if line == " ":
            print("Good eveing Dr. ")
            LastName = "T"
        if LastName == "T":
            print(line)
        if line == "":
          LastName =="F"
    
    DataFile.close()

def Main():
    DataList()
    GoodEvening()

Main() 

   
