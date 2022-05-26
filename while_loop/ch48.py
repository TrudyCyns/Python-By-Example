# Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party.

name = input("Enter a name you want to invite to a party: ")
print(f"{name} has been invited to the party.")

count = 1

ask = input("Do you want to invite another person (y/n): ")
ask = ask.lower()

while ask == "y":
    name = input("Enter another name: ")
    print(f"{name} has been invited to the party.")
    count += 1
    ask = input("Do you want to invite another person (y/n) ")
    ask = ask.lower()

print(f"You have invited {count} people to the party.")
