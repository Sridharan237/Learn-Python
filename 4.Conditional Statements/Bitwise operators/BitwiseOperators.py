# python program to implement bitwise operations like &, |, ~, ^, <<, >> 
 
a = 1
format(a, 'b')              # OUTPUT : '1'
print(format(25, 'b'))      # OUTPUT : 11001
format(30, 'b')             # OUTPUT : '11110'

bin(45)                     # OUTPUT : '0b101101'
print(bin(45))              # OUTPUT : 0b101101

a = 45
print(a.bit_length())       # OUTPUT : 6

# Bitwise operators:

# & -> Bitwise AND
print(5 & 7)                # OUTPUT : 5

# | -> Bitwise OR
print(5 | 7)                # OUTPUT : 7

# ~ -> Bitwise NOT (or) Bitwise complement
print(~5)                   # OUTPUT : -6
print(~-6)                  # OUTPUT : 5
print(~(-6))                # OUTPUT : 5

# ^ -> Bitwise XOR  
print(5 ^ 7)                # OUTPUT : 2

# << -> Bitwise Left Shift Operator
print(10 << 1)              # OUTPUT : 20
print(10 << 2)              # OUTPUT : 40

# >> -> Bitwise Right Shift Operator
print(10 >> 1)              # OUTPUT : 5
print(20 >> 2)              # OUTPUT : 5