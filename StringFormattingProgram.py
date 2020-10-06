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
FileData = DataFile.read()
List = [FileData]


#Output the list in file: Names
def DataList():
    print("--------------------------------")
    print("Names in file Names.txt:")
    print(FileData)
    print("--------------------------------")
    print("Names list in file Names.txt:")
    print (List)
    print()

#Modify the data by adding "Good eveing dr."
def GoodEvening():
    FirstName = ""
    LastName = ""
    Index = 0
    FNBeg = 0
    FNEnd = 0
    print("--------------------------------")
    print("String formatting program output:")
    print()
    for line in FileData:

        if line != " ":
            FirstName += line

        if line == " ":
            FNEnd = Index #Capturing the index of the end of the first name
            
        if line != "\n":
            LastName += line
            Index += 1 #Index counts here to prevent counting a carriage return

        if line == "\n":
            print("Good eveing Dr.",LastName[FNEnd:Index] , "Would you mind if I call you", FirstName[FNBeg:FNEnd], "?")
            FNBeg = Index #Capturing the index of the beginning of the first name

def Main():
    DataList()
    GoodEvening()
    DataFile.close()

Main() 

   
