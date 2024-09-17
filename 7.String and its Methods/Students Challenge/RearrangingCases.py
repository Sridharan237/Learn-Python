# python program to rearrange the cases of a string like : lowercases then uppercases

s = input('Enter a string : ')

lower = ''
upper = ''

for x in s:
    if x.islower():
        lower += x
    elif x.isupper():
        upper += x

lower_upper = lower + upper

print('Rearranged String (lower then upper) :', lower_upper)