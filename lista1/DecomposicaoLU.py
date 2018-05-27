import sys
from substitutions import *
import numpy as np
from copy import deepcopy

A = [[13.5, 7.5, 4.5, 1.5, 3.0, 1.5],
    [7.5, 15.0, 7.5, 4.5, 1.5, 3.0],
    [4.5, 7.5, 13.5, 7.5, 1.5, 3.0],
    [1.5, 4.5, 7.5, 9.0, 1.5, 3.0],
    [3.0, 1.5, 1.5, 1.5, 7.5, 4.5],
    [1.5, 3.0, 3.0, 3.0, 4.5, 6.0]
]

B = [10.0, 20.0, 30.0, 40.0, 30.0, 10.0]

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
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 13],]

    B = [4.0, 0.0, 8.0, 0.0, 12.0, 0.0, 8.0, 0.0, 4.0, 0.0]

    LU = decompLU(A)
    return backSubst(LU, fwdSubst(LU, B))


def resolSist():
    A = [[5.0,-4.0,1.0,0.0],
        [-4.0,6.0,-4.0,1.0],
        [1.0,-4.0,6.0,-4.0],
        [0.0,1.0,-4.0,5.0]
    ]

    B = [-1.0,0.0,1.0,0.0]
    LU = decompLU(A)
    print np.matrix(LU)
    return backSubst(LU, fwdSubst(LU, B))


def resolSistSingular():
    A = [[1.0, 2.0, 2.0], [2.0, 4.0, 4.0], [4.0, 6.0, 4.0]]  # MATRIZ.
    B = [3.0, 6.0, 10.0]  # VETOR INDEPENDNENTE.
    LU = decompLU(A)
    return backSubst(LU, fwdSubst(LU, B))


def decompLU(A):
    n = len(A)
    for k in range(n):
        for i in range(k+1, n):
            try:
                A[i][k] = A[i][k]/A[k][k]
            except:
                sys.exit("ERRO: MATRIZ SINGULAR")
        for j in range(k+1, n):
            for i in range(k+1, n):
                A[i][j] = A[i][j]-A[i][k]*A[k][j]
    return A


def provaReal():
    testeReal = [[1.0, 2.0, 2.0], [4.0, 4.0, 2.0], [4.0, 6.0, 4.0]]
    provaReal = [[1.0, 2.0, 2.0], [4.0, -4.0, -6.0], [4.0, 0.5, -1.0]]
    if decompLU(testeReal) == provaReal:
        return "Ca Marche Bien"
    else:
        return "C'est fou"

def resolveSystem(A, B):
    Acopy = deepcopy(A)
    LU = decompLU(Acopy)
    return backSubst(LU, fwdSubst(LU, B))

# print np.matrix(decompLU(A))

# print resolSist()
