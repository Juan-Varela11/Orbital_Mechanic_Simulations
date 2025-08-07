import scipy
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


# Scientific constants

G = 6.6743e-11 # m^3 kg^-1 s^-2 / gravitational constant 


# Intialize planets
## Working with case of m1 (M) >> m2 (m)
## m orbiting planet M
print("Planet m is orbiting planet M. Condition is that the mass of m is less than the mass of M.")
M = float(input('Mass of planet M (kg): ')); # kg
m = float(input('Mass of planet m (kg): ')); # kg
r_0 = float(input('Initial distance between both objects (m): ')); #m
# Calculations

Fg_0 = (G * m * M)/(r_0**2)
print('The gravitatonal force exerted on planet m by planet M is {:.2e}'.format(Fg_0))


# Initialize grid


# Time-series data initialization

