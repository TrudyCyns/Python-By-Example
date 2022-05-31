# Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until they enter the number that was randomly picked.

import random

num = random.randint(1, 10)
userNum = int(input('Enter a number: '))
while userNum != num:
    userNum = int(input('Enter a number: '))

print(f'{userNum} was chosen.')