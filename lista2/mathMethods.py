import sys


def multiMV(A, X):
    n = len(A)
    Y = [[0.0] for i in range(n)]
    for i in range(n):
        sp = 0.0
        for j in range(n):
            sp += A[i][j]*X[j][0]
        Y[i][0] = sp
    return Y


def multiMM(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise Exception(
            "Cannot multiply the two matrices. Incorrect dimensions.")

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def multiMS(A, b):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            A[i][j] = A[i][j]*b
    return A


def checkSimetricMatrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] == A[j][i]:
                continue
            else:
                sys.exit("ERRO: MATRIZ NAO SIMETRICA!")

# testeReal = [[1.0,0.2,0.0],[0.2,1.0,0.5],[0.0,0.5,1.0]]
# print multiMV(testeReal,[[1.0], [1.4166666666666667], [1.25]])
