# python program to remove duplicates in a list - external, inplace

L1 = [2, 8, 4, 3, 2, 9, 8, 12, 6, 5, 10, 4]     # L1 - list with duplicates

L2 = []     # L2 - list without duplicates

for x in L1:
    if x not in L2:
        L2.append(x)

print('-'*3, 'External', '-'*3)
print('List after removing duplicates :', L2)

# Removing Duplicates - inplace (no extra list should be used)
L1 = [2, 8, 4, 3, 2, 9, 8, 12, 6, 5, 10, 4]     # L1 - list with duplicates

for x in L1:
    if L1.count(x) > 1:
        L1.remove(x)

print('-'*3, 'Inplace', '-'*3)
print('List after removing duplicates :', L1)




