# python program to implement print function - with optional parameters -[sep, end, file, flush]

a = 5
b = 'Akash'
c = 98.3432

print(a, b, c)
print('hello', 'world')
print(a, b, c, sep='*')
print('hello', 'world', sep='*')

print(a)
print(b)
print(c)

print(a, end='-')
print(b, end='-')
print(c, end='-')

print('hello', flush=True)


