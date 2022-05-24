# Ask the user to type in the first line of a nursery rhyme and display the length of the string. Ask for a starting number and an ending number and then display just that section of the text (remember Python starts counting from 0 and not 1).

# Ask for first line of a nursery rhyme
rhyme = input("Please enter first line of a nursery rhyme: ")

# Display length of string
print(len(rhyme))

# Ask for starting number and ending number
sNum = int(input("Please enter a starting number: "))
endNum = int(input("Please enter an ending number: "))

# Print section
print(rhyme[sNum:endNum])
