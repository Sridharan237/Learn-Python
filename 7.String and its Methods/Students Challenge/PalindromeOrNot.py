# python program to check whether a given string is palindrome or not

string = input('Enter a string : ')

reverse = string[::-1]

if reverse == string:
    print('Palindrome')
else:
    print('Not Palidrome')