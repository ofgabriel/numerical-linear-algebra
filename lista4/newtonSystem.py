from functions import *
import sys

tol = 5*10**-4
niter = 10

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def newtonSystem(X, tol, niter, funcs):
    for k in range(niter):
        J = jacobianMatrix(funcs, X)
        print 'J: ' + str(J)
        F = [func(X) for func in funcs]
        print 'F: ' + str(F)
        deltaX = multiMV(J, F)
        print 'deltaX: ' + str(deltaX)
        X = [X[i]+deltaX[i] for i in range(len(X))]
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

X = [2, 3]
funcs = [func1, func2]

newtonSystem(X, tol, niter, funcs)
