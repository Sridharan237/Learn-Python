# python program to implement a function to check if the maximum difference between 2 numbers is 5

# function to check if the maximum difference between 2 numbers is 5
def difference(a, b)-> bool: 
    if abs(a-b) <= 5:
        return True
    return False

print(difference(5, 12))
print(difference(5, 10))