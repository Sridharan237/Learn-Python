# python program to find the occurrences of each item in a list

L1 = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'C', 'A', 'B', 'A']    # L1 - list with duplicates

L2 = []     # L2 - list with each item and its number of occurrences in list L1

for x in L1:
    if x not in L2:
        L2.append(x)
        L2.append(L1.count(x))

print('List with number of occurrences :', L2)
