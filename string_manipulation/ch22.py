# Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.

# Ask for names and assign to variables.
fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")

# Change case to Title Case
fname = fname.title()
lname = lname.title()

# Join names
fullName = fname + " " + lname

# Display finished result
print(fullName)