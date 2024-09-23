# python program to implement nested list to show how to access the elements of the nested list

List = [10, 20, ['a', 'b', ['c', 'd']], 30, 40]

print(List)
# Output : [10, 20, ['a', 'b', ['c', 'd']], 30, 40]

for x in List:
    print(x)
''' 
Output : 
10
20
['a', 'b', ['c', 'd']]
30
40
'''

List[0]
# Output : 10

print(List[2][0])
# Output : 'a'

List[2][2][1]
# Output : 'd'