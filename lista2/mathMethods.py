def multiMV(A,X):
    n = len(A)
    Y = [[0.0] for i in range(n)]
    for i in range(n):
        sp = 0.0
        for j in range(n):
            sp += A[i][j]*X[j][0]
        Y[i][0] = sp
    return Y

def multiMS(A,b):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            A[i][j] = A[i][j]*b
    return A

# testeReal = [[1.0,0.2,0.0],[0.2,1.0,0.5],[0.0,0.5,1.0]]
# print multiMV(testeReal,[[1.0], [1.4166666666666667], [1.25]])