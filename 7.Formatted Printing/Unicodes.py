# python program to implement unicodes

s = '\u03b1'    # '\u03b1' -> utf-16 (2bytes = 16bits)
print(s)   # Output : 'α'

s = '\u03b1\u03b2\u03b3'
print(s)   # Output : 'αβγ'

s = '\u0041'
print(s)   # Output : 'A'

s = '\u0915\u0916\u0917'
print(s)   # Output : 'कखग'

s = 'A'
print(s)   # Output : 'A'

s = '\u0041'
print(s)   # Output : 'A'

# s = '\u41'
#   File "<stdin>", line 1
#     s = '\u41'
#         ^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-3: truncated \uXXXX escape

s = '\x0041'    # '\x0041' - treated as string
print(s)   # Output : '\x0041'

s = '\x41'  # '\x41' -> utf-8 (1byte = 8bits)
print(s)   # Output : 'A'