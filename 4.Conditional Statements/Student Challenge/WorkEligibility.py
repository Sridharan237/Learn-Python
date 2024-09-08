# python program to check whether a person's given age is eligible to work or not   (eligible -> 18-60)

age = int(input('Enter the age : '))

print('Work Eligibility : ', end='')

if age >= 18 and age <= 60:
    print('Eligible')
else:
    print('Not Eligible')