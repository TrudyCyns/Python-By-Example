# Make a maths quiz that asks five questions by randomly generating two whole numbers to make the question (e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At the end of the quiz, tell them how many they got correct out of five.

import random

counter = 0
marks = 0

while counter < 5:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    sum = int(input(f'{num1} + {num2} = '))
    if sum == (num1 + num2):
        marks += 1
    counter += 1

print(f'You got {marks} out of {counter} questions right.')
