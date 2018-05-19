import sys
from substitutions import *
import math
import numpy as np

A = [
    [13.5, 7.5, 4.5, 1.5, 3.0, 1.5],
    [7.5, 15.0, 7.5, 4.5, 1.5, 3.0],
    [4.5, 7.5, 13.5, 7.5, 1.5, 3.0],
    [1.5, 4.5, 7.5, 9.0, 1.5, 3.0],
    [3.0, 1.5, 1.5, 1.5, 7.5, 4.5],
    [1.5, 3.0, 3.0, 3.0, 4.5, 6.0],
]

B = [10.0, 20.0, 30.0, 40.0, 30.0, 10.0]


def resolSistExerc3():
    A = [[13.5, 7.5, 4.5, 1.5, 3.0, 1.5],
         [7.5, 15, 7.5, 4.5, 1.5, 3.0, 5, 4, 3, 2],
         [8, 9, 18, 9, 8, 7, 6, 5, 4, 3],
         [7, 8, 9, 19, 9, 8, 7, 6, 5, 4],
         [6, 7, 8, 9, 18, 9, 8, 7, 6, 5],
         [5, 6, 7, 8, 9, 17, 9, 8, 7, 6],
         [4, 5, 6, 7, 8, 9, 16, 9, 8, 7],
         [3, 4, 5, 6, 7, 8, 9, 15, 9, 8],
         [2, 3, 4, 5, 6, 7, 8, 9, 14, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 13], ]

    B = [4.0, 0.0, 8.0, 0.0, 12.0, 0.0, 8.0, 0.0, 4.0, 0.0]

    LU = decompCholesky(A)
    return fwdSubstitution(LU,backSubst(LU, B))


def resolSist():
    A = [
        [13.5, 7.5, 4.5, 1.5, 3.0, 1.5],
        [7.5, 15.0, 7.5, 4.5, 1.5, 3.0],
        [4.5, 7.5, 13.5, 7.5, 1.5, 3.0],
        [1.5, 4.5, 7.5, 9.0, 1.5, 3.0],
        [3.0, 1.5, 1.5, 1.5, 7.5, 4.5],
        [1.5, 3.0, 3.0, 3.0, 4.5, 6.0],
    ]

    B = [10.0, 20.0, 30.0, 40.0, 30.0, 10.0]
    L = decompCholesky(A)
    LTranspose = np.transpose(np.array(L))
    Y = fwdSubst(L, B)
    X = backSubst(LTranspose, Y)
    return X

def verify(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] == A[j][i]:
                continue
            else:
                sys.exit("ERRO: MATRIZ NAO SIMETRICA!")

def decompCholesky(A):
    verify(A)
    n = len(A)
    L = []
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)

    for i in range(n):
        aux = 0
        for k in range(0, i):
            aux += math.pow(L[i][k], 2)
        try:
            L[i][i] = math.sqrt(A[i][i] - aux)
        except:
            sys.exit("ERRO: MATRIZ NAO POSITIVA DEFINIDA!")
        for j in range(i+1, n):
            aux = 0
            for k in range(0, i):
                aux += L[i][k]*L[j][k]
            L[j][i] = (A[i][j] - aux)/L[i][i]

    return L

def det(A):
    det = 1
    for i in range(len(A)):
        det *= A[i][i]
    print det**2

print det(decompCholesky(A))

print resolSist()
