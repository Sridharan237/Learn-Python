# python program to convert roman to integer
roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

string = input('Enter the roman letters (in upper case): ')

Integer = 0

i = 0

while i < len(string):
    if i+1 < len(string) and roman[string[i]] < roman[string[i+1]]:
        Integer += roman[string[i+1]] - roman[string[i]]
        i += 2
    else:
        Integer += roman[string[i]]
        i += 1

print('Integer :', Integer)
