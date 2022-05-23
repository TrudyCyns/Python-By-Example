# Ask the user to enter three numbers. Add first two, multiply sum by third and display the answer as The answer is [answer].

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

ans = (num1+num2)*num3

print(f'The answer is {ans}')
