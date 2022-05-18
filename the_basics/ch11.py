# Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.

overhun = int(input("Please enter a number over 100: "))
underten = int(input("Please enter a number under 10: "))

into = overhun//underten

print(f'{underten} goes into {overhun} {into} times.')
