from functions import *
import sys
sys.path.append('../lista1/')
from DecomposicaoLU import resolveSystem
sys.path.append('../lista2/')
from mathMethods import multiMM, multiMS

tol = 5*10**-4
niter = 1000

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def broydenSystem(X, tol, niter, funcs):
    J = jacobianMatrix(funcs, X)
    #print 'J: ' + str(J)
    B = J
    F = [func(X) for func in funcs]
    for k in range(niter):
        print k
        deltaX = resolveSystem(B, F)
        deltaX = multVectorScalar(deltaX, -1)
        X = sumVetors(X, deltaX)
        diff = norma(deltaX)/norma(X)
        if(diff < tol):
            print "X: "
            print X
            sys.exit()
        else:
            F2 = [func(X) for func in funcs]
            Y = subtractVetors(F2, F)
            F = F2

            term1 = subtractVetors(Y, multiMV(B, deltaX))
            #print 'term1' + str(term1)
            term2 = multiMM(vector2matrix(term1), transpose(vector2matrix(deltaX)))
            #print 'term2'+ str(term2)
            term3 = 1/multiMV(transpose(vector2matrix(X)), X)[0]
            term4 = multiMS(term2, term3)
            B = sumMatrix(B, term4)

    print("Convergencia nao atingida.")

def func1(X):
    return X[0] + 2*X[1] - 2

def func2(X):
    return X[0]**2 + 4*(X[1]**2) -4

X = [2, 3]
funcs = [func1, func2]
print func1([37.85927729651792, -17.92963864825896])
print func2([37.85927729651792, -17.92963864825896])
#broydenSystem(X, tol, niter, funcs)

def func1Lista(X):
    return 16*(X[0]**4) + 16*(X[1]**4) + (X[2]**4) - 16

def func2Lista(X):
    return X[0]**2 + X[1]**2 + X[2]**2 - 3

def func3Lista(X):
    return X[0]**3 - X[1] + X[2] - 1

#X = [1, 2, 3]
#funcsLista = [func1Lista, func2Lista, func3Lista]
#broydenSystem(X, tol, niter, funcsLista)