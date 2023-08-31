# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: DANIEL ARACKAL
# Section: 563
# Assignment: Lab Topic 2
# Date: 28 08 2023
#
#
# YOUR CODE HERE
#
import math

# Observed positions and times
t1 = 12
t2 = 85
x1 = 8
y1 = 6
z1 = 7
x2 = -5
y2 = 30
z2 = 9

# Interpolation time range
start_time = 30
end_time = 60

# Calculate the increments for each iteration
time_increment = (end_time - start_time) / 4

# Perform interpolation at 5 evenly spaced points
for i in range(5):
    t = start_time + i * time_increment
    
    x = ((x2 - x1) / (t2 - t1)) * (t - t1) + x1
    y = ((y2 - y1) / (t2 - t1)) * (t - t1) + y1
    z = ((z2 - z1) / (t2 - t1)) * (t - t1) + z1
    
    print(f"At time {t:.1f} seconds:")
    print(f"x{i+1} = {x:.15f} m")
    print(f"y{i+1} = {y:.15f} m")
    print(f"z{i+1} = {z:.15f} m")
    
    if i < 4:
        print("-----------------------")
