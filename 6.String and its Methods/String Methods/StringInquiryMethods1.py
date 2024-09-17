# python program to implement the string inquiry methods (or) inspector methods like : isupper, islower, istitle, isalnum, isalpha, isspace, isascii, isidentifier, isprintable, isdecimal, isdigit, isnumeric

# methods1 - isupper, islower, istitle
s = 'HELLO'
print(s.isupper())   # Output : True
print(s.islower())   # Output : False
print(s.istitle())   # Output : False
s = 'hello'
print(s.islower())   # Output : True
print(s.istitle())   # Output : False
s = 'How Are You'
print(s.istitle())   # Output : True
print(s.islower())   # Output : False
s = ''
print(s.isupper())   # Output : False
print(s.islower())   # Output : False
print(s.istitle())   # Output : False
s = 'H'
print(s.isupper())   # Output : True
print(s.islower())   # Output : False
print(s.istitle())   # Output : True

# methods2 - isalnum, isalpha, isspace, isascii
s = 'abcz 123'
print(s.isalnum())   # Output : False
s = 'abc # 123'
print(s.isalnum())   # Output : False
print(s.isascii())   # Output : True
s = 'abcd'
print(s.isalpha())   # Output : True
print(s.isalnum())   # Output : True
s = ''
print(s.isspace())   # Output : False
print(s.isascii())   # Output : True
s = '       '
print(s.isspace())   # Output : True
print(s.isascii())   # Output : True
print(s.isalpha())   # Output : False
s = '\u03b1\u03b2\u03b3M'
print(s)     # Output : 'αβγM'
print(s.isalpha())   # Output : True
print(s.isalnum())   # Output : True
print(s.isascii())   # Output : False

# methods3 - isidentifier, isprintable
s = '1length'
print(s.isidentifier())      # Output : False
s = 'length1'
print(s.isidentifier())      # Output : True
s = 'length-@3'
print(s.isidentifier())      # Output : False
s = 'if'
print(s.isidentifier())      # Output : True
print('elif'.isidentifier())     # Output : True
print('class'.isidentifier())    # Output : True
print('class-1'.isidentifier())      # Output : False
s = 'if'
print(s.isprintable())   # Output : True
s = 'hello how are you'
print(s.isprintable())   # Output : True
s = 'hello \n how are you'
print(s.isprintable())   # Output : False
s = '\u03b1\u03b2\u03b3M'
print(s.isprintable())   # Output : True
s = '\u03b1\u03b2\u03b3'
print(s.isprintable())   # Output : True
print(s.isidentifier())      # Output : True
print(s)     # Output : 'αβγ'

# methods4 - isdecimal, isdigit, isnumeric
s = '123'
print(s.isdecimal())     # Output : True
print(s.isdigit())   # Output : True
print(s.isnumeric())     # Output : True
s = '8\u00b2'
print(s)     # Output : '8²'
print(s.isdecimal())     # Output : False
print(s.isdigit())   # Output : True
print(s.isnumeric())     # Output : True
s = '5\u00BD' # (or) s = '5\u00bd'
print(s)     # Output : '5½'
print(s.isdecimal())     # Output : False
print(s.isdigit())   # Output : False
print(s.isnumeric())     # Output : True
s = '\u0661\u0662\u0663'
print(s)     # Output : '١٢٣'
print(s.isdecimal())     # Output : True
print(s.isdigit())   # Output : True
print(s.isnumeric())     # Output : True