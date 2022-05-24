# Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of whole name.

fname = input("Please enter your first name: ")
lname = input("Please enter your last name: ")

fullName = fname + " " + lname

print(fullName)
print(len(fullName))
