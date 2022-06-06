name = input('Please enter your name: ')

counter = 0

for letter in name.lower():
    if letter == 'a' | | letter == 'e' | | letter == 'i' | | letter == 'o' | | letter == 'u':
        counter += 1

print(f'There are {counter} vowels in your name.')
