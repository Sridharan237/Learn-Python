# python program to implement a function which returns the count of lowercase and uppercase letters as a dictionary

# function which returns the count of lowercase and uppercase letters as a dictionary
def caseCount(string):
    lowerCount, upperCount = 0, 0
    
    for s in string:
        if s >= 'a' and s <= 'z':
            lowerCount += 1
        elif s >= 'A' and s <= 'Z':
            upperCount += 1
    
    return {'lowercase count':lowerCount, 'uppercase count':upperCount}



s = 'abcABC'

print(caseCount(s))