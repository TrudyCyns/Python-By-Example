# Ask the user to enter a number between 1 and 12 and then display the times table for that number.

# Ask user to enter a number between 1 and 12
num = int(input("Please enter a number between 1 and 12: "))

# Display the times table for that number.
for i in range(1, 13):
    pdt = num*i
    print(f"{num} * {i} = {pdt}")
