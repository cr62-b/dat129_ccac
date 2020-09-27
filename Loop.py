# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:56:01 2020

@author: Cliff
"""

"""
c = 0
While (c < 5):
    print(c)
    c = c + 1
"""

"""
Fahrenheit = Celsius x (9/5) + 32
"""

Fahrenheit = 0

# Request data from user
while True:
    try:
        Celsius = float(input("Enter the temperature in Celsius: "))
    except ValueError: # checking for input errors
        print("This is not a number.")
    else:
        break

# Calculate the Tax Tip and Total
Fahrenheit = Celsius * (9 / 5) + 32

# Output the amount of savings
print("Temperature in Fahrenheit:",round(Fahrenheit,2))

print()
input("Press enter to close.")
