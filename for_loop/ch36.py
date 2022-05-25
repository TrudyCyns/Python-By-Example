# Alter program 035 so that it will ask the user to enter their name and a number and then display their name that number of times.

# Ask user to enter name and number
fname = input("Please enter your name: ")
num = int(input("Please enter a number: "))

# Print name (num) times.
for i in range(0,num):
    print(fname)
