# Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they want that number included. If they do, then add the number to the total. If they do not want it included, don’t add it to the total. After they have entered all five numbers, display the total.

# Variable total
total = 0

# Ask user to enter 5 numbers and ask if they want the number included, add to total accordingly.
for i in range(5):
    num = int(input("Please enter a number: "))
    ask = input("Do you want the number included? (yes/no): ")
    ask = ask.lower()
    if ask == "yes":
        total += num;
print(f"The total is {total}.")

