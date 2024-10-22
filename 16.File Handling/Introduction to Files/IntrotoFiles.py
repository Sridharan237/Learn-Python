# python program to implement some basic things about opening, accessing, closing files using python programs

file = open('D:\\Learn-Github-Repositories\\Learn Python Programming - Beginner to Master\\16.File Handling\\Introduction to Files\\MyData.txt', 'r')

# file = open('D:/Learn-Github-Repositories/Learn Python Programming - Beginner to Master/16.File Handling/Introduction to Files/MyData.txt', 'r')  # This also is correct syntax for giving absolute path of a file

str1 = file.read(6)

print(type(str1))   # Output : <class 'str'>
print(str1)

str2 = file.read(10)

print(str2)

str3 = file.read()

print(str3)

file.close()