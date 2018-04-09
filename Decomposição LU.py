import sys

ex3 = [[16, 9, 8, 7, 6, 5, 4, 3, 2, 1],
       [9, 17, 9, 8, 7, 6, 5, 4, 3, 2],
       [8, 9, 18, 9, 8, 7, 6, 5, 4, 3],
       [7, 8, 9, 19, 9, 8, 7, 6, 5, 4],
       [6, 7, 8, 9, 18, 9, 8, 7, 6, 5],
       [5, 6, 7, 8, 9, 17, 9, 8, 7, 6],
       [4, 5, 6, 7, 8, 9, 16, 9, 8, 7],
       [3, 4, 5, 6, 7, 8, 9, 15, 9, 8],
       [2, 3, 4, 5, 6, 7, 8, 9, 14, 9],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 13], ]


def resolSist():
    A = [[1.0, 2.0, 2.0], [4.0, 4.0, 2.0], [4.0, 6.0, 4.0]]  # MATRIZ.
    B = [3.0, 6.0, 10.0]  # VETOR INDEPENDNENTE.
    LU = decompLU(A)
    return backSubst(LU, B)


def resolSistSingular():
    A = [[1.0, 2.0, 2.0], [2.0, 4.0, 4.0], [4.0, 6.0, 4.0]]  # MATRIZ.
    B = [3.0, 6.0, 10.0]  # VETOR INDEPENDNENTE.
    LU = decompLU(A)
    return backSubst(LU, B)


def decompLU(A):
    n = len(A)
    for k in range(n-1):
        for i in range(k+1, n):
            try:
                A[i][k] = A[i][k]/A[k][k]
            except:
                sys.exit("ERRO: MATRIZ SINGULAR")
        for j in range(k+1, n):
            for i in range(k+1, n):
                A[i][j] = A[i][j]-A[i][k]*A[k][j]
    return A


def fwdSubst(LU, B):
    n = len(LU)
    Y = []
    Y.append(B[0]/LU[0][0])
    for i in range(1, n):
        sp = 0
        for j in range(i):
            sp += LU[i][j]*Y[j]
        Y.append((B[i] - sp))
    return Y


def backSubst(LU, B):
    Y = fwdSubst(LU, B)
    n = len(LU)-1
    X = []
    for i in range(n+1):
        X.append(0)
    X[n] = (Y[n]/LU[n][n])
    for i in range(n-1, -1, -1):
        sp = 0
        for j in range(i+1, n+1):
            sp += LU[i][j]*X[j]
        Y.append((B[i] - sp))
    return X


def provaReal():
    testeReal = [[1.0, 2.0, 2.0], [4.0, 4.0, 2.0], [4.0, 6.0, 4.0]]
    provaReal = [[1.0, 2.0, 2.0], [4.0, -4.0, -6.0], [4.0, 0.5, -1.0]]
    if decompLU(testeReal) == provaReal:
        return "Ca Marche Bien"
    else:
        return "C'est fou"


print resolSist()
print resolSistSingular()
