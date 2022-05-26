# Ask how many people the user wants to invite to a party. If then enter a number below 10, ask for the names and after each name display “[name] has been invited”. If they enter a number which is 10 or higher, display the message “Too many people”.

# Ask user to a number
guests = int(input("How many people do you want to invite to a party?: "))

# Check if greater than or less than 10.
if guests < 10:
    for i in range(0,guests):
        invite = input("Enter the name or guest: ")
        print(f"{invite} has been invited.")
else:
    print("Too many people!")  
