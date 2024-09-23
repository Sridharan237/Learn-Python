# python program to implement matrix addition using nested list

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print('A :', A)
print('B :', B)

C = []     # C - sum of two matrices (result)

for i in range(len(A)):
    S = []  # S - list (which stores row sum of two matrices)
    for j in range(len(A[0])):
        S.append(A[i][j]+B[i][j])
    C.append(S)

print('Sum Of Two Matrices :', C)
