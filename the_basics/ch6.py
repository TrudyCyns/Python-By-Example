# Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format.

num1 = int(input("How many slices of pizza did you start with?: "))
num2 = int(input("How many slices of pizza have you eaten so far?: "))

left = num1-num2

print(f'You are left with {left} slices of pizza.')
