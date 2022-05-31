# Randomly choose either heads or tails (“h” or “t”). Ask the user to make their choice. If their choice is the same as the randomly selected value, display the message “You win”, otherwise display “Bad luck”. At the end, tell the user if the computer selected heads or tails.

import random

choose = random.choice(['h', 't'])
makeChoice = input("Choose: head or tails (h/t): ")

if makeChoice == choose:
    print("You win")
else:
    print('Bad Luck!')


print(f'The computer chose {choose}.')