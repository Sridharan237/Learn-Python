# python program to implement the string methods like : replace, join, split, rsplit, splitlines

s = 'a-b-c-d-e'

# replace
print(s)   # Output : 'a-b-c-d-e'
print(s.replace('-', ',')) # Output : 'a,b,c,d,e'
print(s.replace('-', ',')) # Output : 'a,b,c,d,e'
print(s.replace('-', ',', 3))  # Output : 'a,b,c,d-e'
s = 'abcd@gmail.com'
print(s.replace('gmail', 'yahoo')) # Output : 'abcd@yahoo.com'

# join
s1 = 'xyz'
s2 = 'abc'
print(s1.join(s2)) # Output : 'axyzbxyzc'
s1 = '/'
print(s1.join(s2)) # Output : 'a/b/c'
l1 = ['john', 'smith', 'ajay']
s1='-'
print(s1.join(l1)) # Output : 'john-smith-ajay'
s1 = ','
print(s1.join(l1)) # Output : 'john,smith,ajay'

# split
s = 'john smith ajay'
print(s.split())   # Output : ['john', 'smith', 'ajay']
s = 'john  smith ajay'
print(s.split())    # Output : ['john', 'smith', 'ajay']
print(s.split('h')) # Output : ['jo', 'n  smit', ' ajay']
s = 'john, smith, ajay'
print(s.split(','))    # Output : ['john', ' smith', ' ajay']
s = 'john-smith-ajay-khan-james'
print(s.split())   # Output : ['john-smith-ajay-khan-james']
print(s.split('-'))    # Output : ['john', 'smith', 'ajay', 'khan', 'james']
print(s.split('-', 3)) # Output : ['john', 'smith', 'ajay', 'khan-james']

# rsplit
print(s.rsplit('-'))   # Output : ['john', 'smith', 'ajay', 'khan', 'james']
print(s.rsplit('-', 3))    # Output : ['john-smith', 'ajay', 'khan', 'james']

# splitlines
s = 'aaa\nbbb\tccc\rddd\feee'
print(s.splitlines())  # Output : ['aaa', 'bbb\tccc', 'ddd', 'eee']
print(s.splitlines(keepends=True)) # Output : ['aaa\n', 'bbb\tccc\r', 'ddd\x0c', 'eee']
print('hai\feee')
'''
Output : 
hai
eee
'''
print(s.split())   # Output : ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
print(s.split('hello'))    # Output : ['aaa\nbbb\tccc\rddd\x0ceee']