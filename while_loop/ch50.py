# Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.

num = int(input("Please enter number between 10 and 20: "))

while num  < 10 and num > 20:
    if num > 20:
        print("Too high")
        num = int(input("Please enter number between 10 and 20: "))
    elif num < 10:
        print("Too low")
        num = int(input("Please enter number between 10 and 20: "))
        
print("Thank you.")