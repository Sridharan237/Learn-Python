# python program to implement copying binary files in python 
# Here, we are going to copy from one binary file to another binary file
# Binary Files => media files (image, audio, video)

file = open('Python1-logo.jpg', 'rb')

data = file.read()

copy_file = open('Python2-logo.jpg', 'wb')

copy_file.write(data)   # copying file1 to file2

print(data)

file.close()
copy_file.close()
