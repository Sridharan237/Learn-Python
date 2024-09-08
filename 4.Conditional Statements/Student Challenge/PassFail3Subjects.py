# python program to check whether a person passed in all three subjects (marks(in each subject) >= 50) otherwise fail

mark1, mark2, mark3 = int(input('Enter subject1\'s mark : ')), int(input('Enter subject2\'s mark : ')), int(input('Enter subject3\'s mark : '))

if mark1 >= 50 and mark2 >= 50 and mark3 >= 50:
    print('Passed')
else:
    print('Failed')