# Change program 037 to also ask for a number. Display their name(one letter at a time on each line) and repeat this for the number times they entered.

# Ask user to enter name and a number
fname = input("Please enter your name: ")
num = int(input("Please enter a number: "))

# Print each letter on a seperate line
for j in range(0,num):
    for i in fname:
        print(i)
