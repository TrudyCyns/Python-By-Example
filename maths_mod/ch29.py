# Ask the user to enter an integer that is over 500. Work out the square root of that number and display it to two decimal places.

import math


# Ask for a number over 500.
num = int(input("Enter a number over 500: "))

# Find the squareroot of the number.
newNum = math.sqrt(num)

# Display the answer to 2 decimal places.
print(round(newNum, 2))
