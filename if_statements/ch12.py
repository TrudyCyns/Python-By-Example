# Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1 > num2:
    print(num1)
    print(num2)
else:
    print(num2)
    print(num1)
# else:
#     print(f"{num1} and {num2} are equal")