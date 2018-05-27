from functions import *
import sys
sys.path.append('../lista1/')
from DecomposicaoLU import resolveSystem

tol = 5*10**-4
niter = 100

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def newtonSystem(X, tol, niter, funcs):
    for k in range(niter):
        J = jacobianMatrix(funcs, X)
        print 'J: ' + str(J)
        F = [func(X) for func in funcs]
        print 'F: ' + str(F)
        deltaX = resolveSystem(J, F)
        deltaX = multVectorScalar(deltaX, -1)
        print 'deltaX: ' + str(deltaX)
        X = sumVetors(X, deltaX)
        diff = norma(deltaX)/norma(X)
        if(diff < tol):
            print "X: "
            print X
            sys.exit()

    print("Convergencia nao atingida.")

def func1(X):
    return X[0] + 2*X[1] - 2

def func2(X):
    return X[0]**2 + 4*(X[1]**2) -4

#X = [2, 3]
#funcs = [func1, func2]
#newtonSystem(X, tol, niter, funcs)

def func1Lista(X):
    return 16*(X[0]**4) + 16*(X[1]**4) + (X[2]**4) - 16

def func2Lista(X):
    return X[0]**2 + X[1]**2 + X[2]**2 - 3

def func3Lista(X):
    return X[0]**3 - X[1] + X[2] - 1

X = [1, 2, 3]
funcsLista = [func1Lista, func2Lista, func3Lista]
newtonSystem(X, tol, niter, funcsLista)