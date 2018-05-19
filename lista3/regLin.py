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

def testeReglin(X):
    for i in range(len(X)):
        X[i].append(2.38698300737*X[i][0] + 12.2376723309)
    print X

print regLin([[-2.70],[-1.00],[0.00],[1.0],[1.60],[3.10]],[[6.00],[9.20],[12.00],[15.00],[17.00],[19.00]])
print testeReglin([[-2.70],[-1.00],[0.00],[1.0],[1.60],[3.10]])
