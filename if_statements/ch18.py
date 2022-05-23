# Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.

num1 = int(input("Enter a number: "))

if num1 < 10:
    print("Too low!")
elif num1 >= 10 and num1 <= 20:
    print("Correct.")
else:
    print("Too high!")
