# Update program 056 so that it tells the user if they are too high or too low before they pick again.

import random

num = random.randint(1, 10)
userNum = int(input('Enter a number: '))

while userNum != num:
    if userNum > num:
        print('Too high.')
        userNum = int(input('Enter a number: '))
    else:
        print('Too low.')
        userNum = int(input('Enter a number: '))
   
print(f'{userNum} was chosen.')