from cmath import sqrt
import math
print("Welcome to the velocity calculator. Please enter the following:\n")
m= float(input("Mass(in kg):"))
g= float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Juptiter):"))
t= float(input("Time (in seconds):"))
density= float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water):"))
cross_area= float(input("Cross sectional area (in m^2):"))
drag= float(input("Drag constant (0.5 for sphere, 1.1 for cylinder):"))
c= (1 / 2) * density * cross_area * drag
veloctiy= math.sqrt(m * g / cross_area) * (1- math.exp((-math.sqrt(m * g * cross_area) / m) * t ))
print(" ")
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {veloctiy:.3f} m/s")
print(" ")
print("Are you curious to see how the velocities differ dpepnding on the gravitational pull? Let's find out")
earth= 9.8
jupiter= 24
velocity_earth= math.sqrt(m * earth / cross_area) * (1- math.exp((-math.sqrt(m * earth * cross_area) / m) * t ))
print(f"The velocity for Earths gravity: {velocity_earth:.3f}")
velocity_jupiter= math.sqrt(m * jupiter / cross_area) * (1- math.exp((-math.sqrt(m * jupiter * cross_area) / m) * t ))
print(f"The velocity for Jupiter'gravity: {velocity_jupiter:.3f}")
difference= velocity_jupiter - velocity_earth
print(f"The difference in velocity's is: {difference:.3f} m/s")