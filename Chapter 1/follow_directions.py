# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: DANIEL ARACKAL
# Section: 563
# Assignment: Lab Topic 1 - Activity 3
# Date: 22 08 2023
#
#
# YOUR CODE HERE
#

import math

#array of numbers ranging from 1.1 to 1.00000001
x = [1.1, 1.01, 1.001, 1.0001, 1.00001, 1.000001, 1.0000001, 1.00000001]

print("This shows the evalutaion of sin(x-1) / (x-1) evaluated close to x = 1")
print("My guess is that it will reach 1")

#for loop
for y in x:
    result = (math.sin(y - 1))/(y - 1)
    print(result)

print("My guess was accurate")
