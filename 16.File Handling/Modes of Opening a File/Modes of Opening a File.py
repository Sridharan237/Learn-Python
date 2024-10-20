# python program to implement various modes in opening a text file (r, w, a, r+, w+, a+, x)

# Example 1 => r(read mode)
file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Modes of Opening a File\\MyData.txt', 'w')

file.write('hello hai welcome\n')
file.write('This is time\n')
file.write('It is a file\n')

file.close()

# Example 2 => a(append mode)
file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Modes of Opening a File\\MyData.txt', 'a')

file.write('appending content1\n')
file.write('appending content2')

file.close()

# # Example 3 => x(exclusive creation)
# file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Modes of Opening a File\\Exclusive Creation.txt', 'x')

# file.write('appending content1\n')
# file.write('appending content2')

# file.close()

# Example 4 => r+ (read, write) - read has higher priority - means it will cause FileNotFoundError if the file does not exist
file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Modes of Opening a File\\MyData.txt', 'r+')

str1 = file.read(5)

print(str1)

str1 = file.read()

print(str1)

file.close()

# Example 5 => w+ (write, read) - write has higher priority - means it will create a file if it does not exist
file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Modes of Opening a File\\MyData.txt', 'w+')

file.write('hello\n')
file.write('hai\n')
file.write('welcome\n')

str1 = file.read()

print(str1)

file.close()

# Example 6 => a+ (append, read) - append has higher priority - means it will cause error if the file does not exist
file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Modes of Opening a File\\MyData.txt', 'a+')

file.write('hello1\n')
file.write('hai1\n')
file.write('welcome1\n')

str1 = file.read()

print(str1)

file.close()