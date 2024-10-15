# python program to implement a function which prints the pascal triangle pattern

def pascalTriange(n):
    print('-'*3+' Pascal\'s Triangle '+'-'*3)
    row = [1]
    print(row)
    
    for i in range(n-1):
        temp_row = [0] + row
        row.append(0)
        new_row = list(map(lambda x, y : x+y, row, temp_row))
        print(new_row)
        
        row = new_row
    
    
n = int(input('Enter the value for n : '))
pascalTriange(n)