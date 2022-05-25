# Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work out the area of the circle(π*radius2).

import math

# Ask for radius of a circle.
radius = float(input("Please enter the radius of a circle:"))

# Workout area of the circle.
area = (math.pi) * (radius**2)
print(area)