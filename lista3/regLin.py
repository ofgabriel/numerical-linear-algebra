import mathMethods as m
import numpy as np

def regLin(X,Y):
    #Returns the paramaters 'a' & 'b' for a linear regression of a 'x' & 'y' set.
    P = []
    for i in range(len(X)):
        P.append([1.0,X[i][0]])
    PTranspose = np.transpose(np.array(P))
    A = m.multiMM(PTranspose,P)
    C = m.multiMV(PTranspose,Y)
    B = m.multiMM(np.linalg.inv(np.array(A)),C)

    print 'Coef. Angular = ' + str(B[1][0]) + ', Coef. Linear = ' + str(B[0][0])

print regLin([[1.00],[2.00],[3.00]],[[2.00],[3.50],[6.50]])
