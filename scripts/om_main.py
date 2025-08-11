import scipy
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

'''
References:
* http://www.braeunig.us/space/orbmech.htm
* https://proceedings.scipy.org/articles/majora-212e5952-015
* Carroll, B. W., & Ostlie, D. A. (2017). An Introduction to Modern Astrophysics (2nd ed.).
  Cambridge: Cambridge University Press. 
* Hintz, G.R. (2022). Orbital mechanics and astrodynamics : techniques and tools for space missions. Springer.
* Fukushima, T. (2025). Position and motion of celestial bodies. Springer Nature Singapore. 
* Bannikova, E., & Capaccioli, M. (2022). Foundations of Celestial Mechanics. Graduate Texts in Physics. Springer.

'''

# Scientific constants

G = 6.6743e-11 # m^3 kg^-1 s^-2 / gravitational constant 


# Intialize planets
## Working with case of m1 (M) >> m2 (m)
## m orbiting planet M
print("Planet m is orbiting planet M. Condition is that the mass of m is less than the mass of M.")
M = float(input('Mass of planet M (kg): ')); # kg; earth is 5.97e24
m = float(input('Mass of planet m (kg): ')); # kg; moon is 7.35e22
r_0 = float(input('Initial distance between both objects (m): ')); #m; earth <-> moon is 384.4e6 

'''
To mathematically describe an orbit one must define six quantities, called orbital elements. They are
- Semi-Major Axis, a
- Eccentricity, e (0 <= e <= 1)
- Inclination, i (0 degrees == prograde (same as primary's rotation); 90 == polar orbit; 180 == retrogade (opposite as primary's rotation))
- Argument of Periapsis, omega
- Time of Periapsis Passage, T
- Longitude of Ascending Node, Omega
'''

a = 1 # placeholder value 

e= 0.5 # elliptical orbit 

inclin = scipy.constants.pi/6 # i of 30 degrees (pi/6 in radians) 

omega = 1 # placeholder value

T = 1 # placeholder value 

Omega = 1 # placeholder value 

# Calculations

Fg_0 = (G * m * M)/(r_0**2)
print('The gravitatonal force exerted on planet m by planet M is {:.2e}'.format(Fg_0))




# Initialize grid

## Origin is at center of planet being orbited 

# Time-series data

t_data = [i for i in range(int(3.154e7+1))] # 1 year in seconds to start (3.154e7)
