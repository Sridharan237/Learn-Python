# python program to check the elgibility to vote for a canditate with respect to age criteria

age = int(input('Enter age : '))

print('Eligibility for voting : ', end='')

if age >= 18:
    print('Eligible')
else:
    print('Not Eligible')