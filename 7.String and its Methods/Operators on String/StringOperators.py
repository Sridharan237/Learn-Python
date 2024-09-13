# python program to implement operators used for performing operation on string

s1 = 'hello'
s2 = 'world'
s3 = s1 + s2
print(s3)   # Output : helloworld

# s3 = s1 s2
#   File "<stdin>", line 1
#     s3 = s1 s2
#             ^^
# SyntaxError: invalid syntax

s3 = 'Hello' 'World'
print(s3)   # Output : HelloWorld

# s4 = 'Hello' + 15
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

s3 = 'Hello' + str(15)
print(s3)   # Output : Hello15

s5 = 'How ' + 'are ' + 'you?'
print(s5)   # Output : How are you?

s1 = 'hi'
print(s1 * 3)   # Output : hihihi

# print(s1 * 2.5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can't multiply sequence by non-int of type 'float'

s6 = 'Hello World'
print(len(s6))  # Output : 11

for i in range(0, len(s6)):
    print(s6[i])

# Output :-
# H
# e
# l
# l
# o

# W
# o
# r
# l
# d

for i in range(len(s6)-1, -1, -1):
    print(s6[i])
    
# Output :-
# d
# l
# r
# o
# W

# o
# l
# l
# e
# H

for i in range(0, len(s6), 2):
    print(s6[i])

# Output : 
# H
# l
# o
# W
# r
# d

s6 = 'Hello World'

print(s6[0:len(s6):1])  # Output : Hello World
print(s6[:len(s1):1])   # Output : He
print(s6[:len(s6):1])   # Output : Hello World
print(s6[::1])          # Output : Hello World
print(s6[::])           # Output : Hello World
print(s6[3::])          # Output : lo World
print(s6[6::])          # Output : World
print(s6[6:8:])         # Output : Wo
print(s6[::2])          # Output : HloWrd
print(s6[::-1])         # Output : dlroW olleH
print(s6[-1:-len(s6)-1:-1]) # Output : dlroW olleH
print(s6[-1::-1])       # Output : dlroW olleH
print(s6[-1::-2])       # Output : drWolH
print('H' in s6)        # Output : True
print('h' in s6)        # Output : False
print('H' not in s6)    # Output : False
print('h' not in s6)