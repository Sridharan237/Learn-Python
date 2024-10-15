# python program to implement a functin which returns minimum number in a list which should be minimum in the list and greater than or equal to low_limit

def minNumLimit(*args, low_limit=None) -> int:
    min = args[0]
    
    for i in range(1, len(args)):
        if args[i] < min and low_limit == None:
            min = args[i] 
        elif args[i] < min and low_limit != None and args[i] >= low_limit:           
            min = args[i]
            
    return min

print(minNumLimit(1, 2, 3, -5, 10, -15))
print(minNumLimit(1, 2, 3, -5, 10, -15, low_limit=1))