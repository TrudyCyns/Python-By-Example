# Ask for the radius and the depth of a cylinder and work out the total volume(circle area*depth) rounded to three decimal places.

# Ask for a radius and depth of a cyliner.
import math


rad = float(input("Enter the radius of a cylinder: "))
dep = float(input("Enter the depth of a cylinder: "))

# Work out the total volume rounded to 3dp.
vol = ((math.pi) * (rad**2))*dep

# Display the answer.
print(round(vol,3))
