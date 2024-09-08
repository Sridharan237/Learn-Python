# python program to check whether a given lower case character is vowel or consonant

ch = input('Enter a lowercase character : ')

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print('Vowel')
elif ch >= 'a' and ch <= 'z':
    print('Consonant')
else:
    print('Invalid lowercase alphabet')