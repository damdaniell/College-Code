# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: DANIEL ARACKAL
# Section: 563
# Assignment: Lab Topic 1 - Activity 2
# Date: 22 08 2023
#
#
# YOUR CODE HERE
#
import math

# A) Calculate the force in Newtons applied to an object with mass 27 kg and acceleration 1.5 m/s^2.
# According to Newton’s Second Law the net force applied to an object produces a proportional
# acceleration.

mass = 27  # in kg
acceleration = 1.5  # in m/s^2

force = mass * acceleration

print("Force is", force, "N")


# B) Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between
# crystal layers of 0.025 nm, scattering angle of 35 degrees, and first order diffraction. Bragg’s Law
# describes the scattering of waves from a crystal using the equation
# 𝑛𝜆 = 2𝑑 𝑠𝑖𝑛 𝜃
# The standard unit of wavelength in the SI system is nanometers (nm).

d = 0.025
theta = math.radians(35) # degrees to radians
n = 1

wavelength = (2 * d * math.sin(theta)) / n

print("Wavelength is", wavelength, "nm")


# C) Calculate how much Radon-222 is left after 5 days of radioactive decay given an initial amount
# of 27 g and a half-life of 3.8 days. The equation for radioactive decay is
# 𝑁(𝑡) = 𝑁02−𝑡/𝑡1/2
# where 𝑁0 is the intial amount (units of grams), 𝑡 is the time (units of days), and 𝑡1/2 is the half-
# life (units of days).

weight = 27 #grams
half_life = 3.8 #days
time_length = 5 #days

radon_left = weight * 2 ** (-time_length / half_life)
print("Radon-222 left is", radon_left, "g")


# D) Calculate the pressure of 5 moles of an ideal gas with a volume of 0.27 m^3, and temperature of
# 415 K. The Ideal Gas Law is the equation of state of a hypothetical ideal gas and is a good
# approximation of the behavior of gases under many conditions. Use a value of 8.314
# m^3Pa/K·mol for the gas constant. The standard unit of pressure in the SI system is kilopascals
# (kPa).

#Find Pressure in kPa

volume = 0.27 #m^3
num_of_moles = 5 #moles
temp = 415 #kelvin
gas_constant = 8.314 #m^3Pa/K·mol

temp = 415 #kelvin
pressure = ((num_of_moles * gas_constant * temp) / volume) / 1000

print("Pressure is", pressure, "kPa")


