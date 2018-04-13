import mathMethods as m

def powerMethod(A):
    tol = 10**(-3)
    n = len(A)
    X0 = [[1.0] for i in range(n)]
    Y = m.multiMV(A,X0)
    ld0 = X0[0][0]
    ld1 = Y[0][0]
    X1 = m.multiMS(Y,(1/ld1))
    R = abs(ld1-ld0)/abs(ld1)
    while R > tol:
        Y = m.multiMV(A,X1)
        ld0 = ld1
        ld1 = Y[0][0]
        X1 = m.multiMS(Y,(1/ld1))
        R = abs(ld1-ld0)/abs(ld1)
    print ld1


testeReal = [[1.0,0.2,0.0],[0.2,1.0,0.5],[0.0,0.5,1.0]]
print powerMethod(testeReal)