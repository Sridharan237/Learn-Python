# python program to implement the basic things on a string

s = 'Hello'
print(type(s))  # Output : <class 'str'>
print(s[1])     # Output : e
print(s[-4])    # Output : e

s1 = 'hello'
s2 = input('Enter a string : ')     # Output : Enter a string : haiwaibai
print(len(s2))  # Output : 9

s1 = 'Hello'
for x in s1:
    print(x, end=' ')       # Output : H e l l o 
    
ch = 'a'
ch = "A"
print(ch)   # Output : A

s1 = 'hello'

# s2 = "hello'
#   File "<stdin>", line 1
#     s2 = "hello'
#          ^
# SyntaxError: unterminated string literal (detected at line 1)

s2 = "hello"
s3 = """ multi
            line
               string
                  literal"""
print(s3)
# Output :  multi
#                 line
#                    string
#                       literal

s4 = ''' multi
line
string
literal'''
print(s4)
# Output :  multi
# line
# string
# literal

# s5 = 'john's'
#   File "<stdin>", line 1
#     s5 = 'john's'
#                 ^
# SyntaxError: unterminated string literal (detected at line 1)

s5 = "john's"
print(s5)   # Output : john's

# s6 = "john\"s'
#   File "<stdin>", line 1
#     s6 = "john\"s'
#          ^
# SyntaxError: unterminated string literal (detected at line 1)

s5 = 'john\'s'
s6 = "john\"s"
print(s5)   # Output : john's
print(s6)   # Output : john"s