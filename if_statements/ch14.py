# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”.

num1 = int(input("Enter a number between 10 and 20: "))

if num1 >= 10 and num1 <= 20:
    print("Thank you.")
else:
    print("Incorrect answer!")
