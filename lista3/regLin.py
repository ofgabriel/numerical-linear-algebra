import mathMethods as m
import numpy as np

def regLin(X,Y):
    #Returns the paramaters 'a' & 'b' for a linear regression of a 'x' & 'y' set.
    P = []
    for i in range(len(X)):
        P.append([1.0,X[i]])
    PTranspose = np.transpose(np.array(P))
    A = m.multiMM(PTranspose,P)
    print A
    C = m.multiMM(PTranspose,Y)
    B = np.linalg.inv(np.array(A))



print regLin([1.00,2.00,3.00],[2.00,3.50,6.50])
