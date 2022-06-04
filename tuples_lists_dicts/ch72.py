subjects = ['Maths', 'Science', 'Biology',
            'Chemistry', 'English', 'Literature']

print(subjects)

toDelete = input('Which of the subjects above do you dislike: ').capitalize()

subjects.remove(toDelete)
print(subjects)
