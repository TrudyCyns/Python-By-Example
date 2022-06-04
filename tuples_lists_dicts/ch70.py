countries = ('Uganda', 'Kenya', 'Tanzania', 'USA', 'UK')

print(countries)

choice = input('Please enter a country from the list above: ')
print(countries.index(choice))

indexChoice = int(input('Please enter a number: '))
print(countries[indexChoice])
