# python program to check whether the marks are valid or not - (valid marks(marks within range 0-100), otherwise invalid)

marks = int(input('Enter the marks : '))

print('Marks :', end='')

if marks >= 0 and marks <= 100:
    print('Valid')
else:
    print('Invalid')