# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: DANIEL ARACKAL
# DALTON SIMMS
# ALEXANDRA SAUVAGE
# AOIFE BRIDGEMAN
# Section: 563
# Assignment: LAB TOPIC 2
# Date: 30 8 2023
#
#
# YOUR CODE HERE
#
#

#Part 1
import math

t1 = 10
t2 = 55
x1 = 2027
x2 = 23027

p = ((x2 - x1) / (t2 - t1)) * (25 - t1) + x1

print("Part 1:")
print("For t = 25 minutes, the position p =", p, "kilometers")


#Part 2

t1 = 10
t2 = 55
x1 = 2027
x2 = 23027
r = 6745

x = ((x2 - x1) / (t2 - t1)) * (300 - t1) + x1

cir = 6 * math.pi * r

p = x - cir

print("Part 2:")
print("For t = 300 minutes, the position p =", p, "kilometers")
