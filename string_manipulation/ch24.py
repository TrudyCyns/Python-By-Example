# Ask the user to enter their first name. If the length of their first name is under five characters, ask to enter their surname and join them together(without a space) and display the name in upper case. If the length of the first name is five or more characters, display their first name in lower case.

# Ask for first name
fname = input("Please enter your first name: ")

# Check for length
if len(fname) < 5:
    lname = input("Please enter your last name: ")
    # Joins names
    fullName = fname + lname
    # Display in uppercase
    print(fullName.upper())
else:
    print(fname.lower())

