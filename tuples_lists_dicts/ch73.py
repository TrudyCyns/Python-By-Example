food={}

for i in range(1,5):
    foodEntry = input('Enter a favorite food: ')
    food[i] = foodEntry

print(food)

toDelete = int(input('Which one do you want to get rid of?: '))

del food[toDelete]

print(sorted(food.values()))