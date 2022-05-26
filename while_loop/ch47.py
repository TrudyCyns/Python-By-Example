# Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. Once the loop has stopped, display the total

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

ask = input("Do you want to add another number? (y/n): ")
ask = ask.lower()

while ask == "y":
    num = int(input("Enter another number: "))
    sum += num
    ask = input("Do you want to add another number? (y/n): ")
    ask = ask.lower()

print(f"The total is {sum}.")
