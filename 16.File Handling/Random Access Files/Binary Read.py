# python program to implement random accessing in binary files (mainly reading from binary file)

# Example 1
with open('file.data', 'rb') as f:
    print(f.read(2).decode())    # Output : ab
    
    # whence = 0 -> sets the file pointer to the beginning of the file
    print('Position :', f.seek(3, 0))   # Output : Position : 3
    
    print(f.read(1).decode())    # Output : d
    
    print('Position :', f.tell())       # Output : Position : 4
    
    # whence = 1 -> sets the file pointer to the current position of the file
    print('Position :', f.seek(2, 1))   # Output : Position : 6
    
    print(f.read(1).decode())    # Output : g
    
    print('Position :', f.tell())       # Output : Position : 7
    
    # whence = 1 -> sets the file pointer to the end position of the file
    print('Position :', f.seek(-2, 2))   # Output : Position : 8
    
    print(f.read(1).decode())    # Output : i
    
    print('Position :', f.tell())       # Output : Position : 9
    
    