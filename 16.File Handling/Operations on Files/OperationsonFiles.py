# python program to implement various operations on files => (read, readline, readlines, write, writelines, close, readable, writeable, tell, seek) and some properties of file object => (name, mode, closed)

# Some properties of file object => name, mode, closed
file = open('file.txt', 'r')

print(type(file))   
# Output : <class '_io.TextIOWrapper'>

print(file.name)    # Output : file.txt
print(file.mode)    # Output : r
print(file.closed)  # Output : False

file.close()

print(file.closed)  # Output : True

# # Binary Files
# file = open('file.txt', 'w')

# print(type(file))   
# # Output : <class '_io.BufferedWriter'>


# read
file = open('file.txt', 'r')

print('File Contents :\n', file.read(), sep='')

file.close()

# readline
file = open('file.txt', 'r')

print('File Contents :\n', file.readline())
print('File Contents :\n', file.readline())
print('File Contents :\n', file.readline())
print('File Contents :\n', file.readline())
print('File Contents :\n', file.readline())

file.close()

# readlines
file = open('file.txt', 'r')

print(file.readlines())
# Output : ['This is a text file.\n', 'Hi Hello Welcome.\n', 'File is a permanent storage.\n', 'File is stored in hard disk.']

file.close()

# Example 1 => read contents in a file line by line
# readlines
file = open('file.txt', 'r')

lines = file.readlines()

for line in lines:
    print(line, end='')

file.close()

# write 
file = open('file.txt', 'w')

str1 = 'hai hello welcome\nThis is cinema\nThis is life'

file.write(str1)

file.close()

# writelines
file = open('file.txt', 'w')

list1 = ['hai hello welcome.\n' ,'This is cinema.\n', 'This is life.']

file.writelines(list1)   

# readable
print(file.readable())

# writeable
print(file.writable())

# tell
print('Tell :', file.tell())    
# Output : 50

# method of file object - to close a file
file.close() 