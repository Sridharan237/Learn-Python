# python program to add 2 matrices (nested list)

A = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
B = [[5, 6, 7, 8], [5, 6, 7, 8], [5, 6, 7, 8]]

C = []

if len(A) == len(B) and len(A[0]) == len(B[0]):
    for i in range(len(A)):
        S=[]
        for j in range(len(A[0])):
            S.append(A[i][j]+B[i][j])
        C.append(S)

print('Result of Addition of 2 Matrices :', C)