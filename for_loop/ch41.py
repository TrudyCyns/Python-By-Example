# Ask the user to enter their name and a number. If the number is less than 10, then display their name that number of times otherwise display the message “Too high” three times.

# Ask user to enter name and a number
fname = input("Please enter your name: ")
num = int(input("Please enter a number: "))

# Check if num is less than 10.
if num<10:
    for i in range(0, num):
        print(fname)
else:
    for i in range(0, 3):
        print("Too high!")
