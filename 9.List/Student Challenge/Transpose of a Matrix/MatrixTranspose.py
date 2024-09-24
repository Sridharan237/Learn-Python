# python program to find the transpose of a matrix using nested lists

A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]  # A - Matrix of Dimension (3 X 4)

T = []  # T - Transpose of Matrix A

for i in range(len(A[0])):
    S = []  # S - each row of Matrix T
    for j in range(len(A)):
        S.append(A[j][i])
    T.append(S)

print('Transpose of Matrix A :', T)