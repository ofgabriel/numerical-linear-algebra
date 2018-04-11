import sys
from substitutions import *
import math
import numpy as np


def resolSistExerc3():
    A = [[16, 9, 8, 7, 6, 5, 4, 3, 2, 1],
         [9, 17, 9, 8, 7, 6, 5, 4, 3, 2],
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
    print LU
    print 'a'
    return backSubst(LU, B)


def resolSist():
    A = [[1.0, 0.2, 0.4], [0.2, 1, 0.5], [0.4, 0.5, 1.0]]  # MATRIZ.
    print np.linalg.cholesky(np.array(A))
    B = [0.6, -0.3, -0.6]  # VETOR INDEPENDNENTE.
    LU = decompCholesky(A)
    # return backSubst(LU, B)


def decompCholesky(A):
    n = len(A)
    L = []
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)

    for i in range(n):
        aux = 0
        for k in range(1, i):
            aux += math.pow(L[i][k], 2)
        L[i][i] = math.sqrt(A[i][i] - aux)

        for j in range(i+1, n):
            aux = 0
            for k in range(1, i):
                aux += L[i][k]*L[j][k]
            L[j][i] = (A[i][j] - aux)/L[i][i]

    print L
    return L


print resolSist()
