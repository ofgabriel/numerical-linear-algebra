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
        Y.append((B[i] - sp)/LU[i][i])
    return X
