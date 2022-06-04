numbers = [345, 765, 980, 435]
for i in numbers:
    print(i)

num = int(input('Enter a 3-digit number: '))
for i in numbers:
    if num == i:
        print(numbers.index(i))
    else:
        print('That is not in the list')
