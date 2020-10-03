# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:36:26 2020

@author: Cliff

Dat-129 Python 2 Programming
Assignment Icon Manipulation
Week 1: 09-02-2020
Clifford B. Rohal

Program to minipulate an icon using one type of character to a different type
of character

"""
#Testing using branch Master

#Bit sequence
bseq = (1,1,1,1,1,1,1,1,1,1,
        0,1,0,0,0,0,0,0,1,0,
        0,0,1,0,0,0,0,1,0,0,
        0,0,0,1,0,0,1,0,0,0,
        0,0,0,0,1,1,0,0,0,0,
        0,0,0,0,1,1,0,0,0,0,
        0,0,0,1,0,0,1,0,0,0,
        0,0,1,0,0,0,0,1,0,0,
        0,1,0,0,0,0,0,0,1,0,
        1,1,1,1,1,1,1,1,1,1)
exp = 0

#Expand the matrix
def displayMatrix():
    count = 1
    exp = int(input("How may times should the list be expanded? "))
    ret = 10 * exp
    for value in bseq:
        for pos in range(0,exp):
            if value == 1:
                print ("*", end='')
            else:
                print (" ", end='')
            if count == (ret):
                print()
                count = 0
            count = count + 1
  
def main():
    print()
    print("----------------------------")
    print()
    print("Printing Icon")
    displayMatrix()    

main()

  