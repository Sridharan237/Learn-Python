# python program to convert a given string to a palindrome -> by concatenation the reverse of the string with itself

string = input('Enter a string : ')

reverse = string[::-1]

palindrome = string + reverse

print('Palindrome :', palindrome)