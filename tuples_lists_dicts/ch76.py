three = 0;
names = []

while three < 3:
    name = input('Please input a name of a person to invite: ')
    names.append(name)
    three += 1

print(names, three)
ask = input('Do you want to add another?(yes/no): ').lower()

while ask == 'yes':
    
    name = input('Please input a name of a person to invite: ')
    names.append(name)
    ask = input('Do you want to add another?(yes/no): ').lower()
    three += 1

print(len(names))