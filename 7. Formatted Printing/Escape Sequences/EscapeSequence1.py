# python program to implement escape sequences - for formatted printing (\n, \t, \r, \v, \f)

print('abc')
print('def')
print('abc\nghi', end='')   # By default, end = '\n' -> 1 newline -> (separator argument)
print('abc\nghi', end='*')
print('abc\tghi', end='')
print('abc\rghi')
print('abc\fghi')
print('abc\vghi')

print('def', 'kmn')
print('def', 'kmn', sep='') # By default, sep = ' ' -> 1 space -> (separator argument)
print('def', 'kmn', sep='*')

# Formatted Printing - using \n, \t

print('\t\t\t\tWelcome')
print('\t\t\t\t1.Akash')
print('\t\t\t\t2.Virat')
print('\t\t\t\t3.Mukesh')