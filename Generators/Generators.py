# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:50:48 2020

@author: Cliff
"""

#Generator/Filter
#-------------------------------------------------------
#Generator using the filter function
#The gererator prints a list of all numerical value and filters out the
#strings.
my_list = [1,"x",2,"y","3","z",3]

def my_int(x):
    #The isinstance() function returns True if the specified object is of
    #the specified type, otherwise False. 
    new_int = isinstance(x, int) 
    return new_int

filter_list = filter(my_int, my_list)

print(list(filter_list))

#Generator/Filters
#-------------------------------------------------------
#Generator using the filter function simplified
#The gererator prints a list of all integers and filters out the strings.
#This simplified version returns the isinstance of x that are integers
my_list = [1,"x",2,"y","3","z",3]

def my_int(x):
    #The isinstance() function returns True if the specified object is
    #of the specified type, otherwise False.    
    return isinstance(x, int)

filter_list = filter(my_int, my_list)

print(list(filter_list))

#Generator/Map
#-------------------------------------------------------
#Generator using the map function more simplified
#Converting strings into integers
my_list = ["1", "2", "3"]

def my_int(x):
    new_var = int(x) 
    return new_var 

my_map = map(my_int, my_list)
my_new_map = list(my_map)

print(my_new_map)

#Generator using the map function simplified
#Converting strings into integers
my_list = ["1", "2", "3"]

def my_int(x):
    return int(x) #new_var = int(x) optional 

my_map = map(my_int, my_list)

print(list(my_map))


#Generator/Map/Lamda
#-------------------------------------------------------
#Generator map using lambda function
#Converting strings into integers
my_list = ["1", "2", "3"]

print(list(map(lambda x: int(x),my_list)))







