# python program to implement a function which returns an integer sum of scores where score ending with zero only be included

from typing import *

# function which returns an integer sum of scores where score ending with zero only be included
def SumScoresEnd0(scores:List[int]) -> int:
    sum = 0
    
    for x in scores:
       if x % 10 == 0:
           sum += x
           
    return sum

L = [200, 456, 300, 100, 234, 678]  # L - scores

print('Sum of Scores End with 0 :', SumScoresEnd0(L)) 