# Display the following message: If the user enters 1, then it should ask them for the length of one of its sides and display the area. If they select 2, it should ask for the base and height of the triangle and display the area. If they type in anything else, it should give them a suitable error message.

# Display Message.
print("""
    1) Square
    2) Triangle
""")
num = int(input("Enter a number: "))

# Check choice
if num == 1:
    side = int(input("Enter the length of one of the sides: "))
    area = side**2
    print(f"The area of the square is {area}.")
elif num==2:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = (1/2)*base*height
    print(f"The area of the triangle is {area}.")
else:
    print("Wrong input!")
