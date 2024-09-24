# python program to find the overlapping elements of 2 lists

L1 = [10, 4, 2, 6, 3, 7, 5]
L2 = [19, 12, 11, 8, 5, 3, 2, 6]

L3 = []     # L3 - list to store the overlapping elements of lists L1 and L2

for x in L1:
    if x in L2:
        L3.append(x)

print('Overlapping Elements :', L3)
