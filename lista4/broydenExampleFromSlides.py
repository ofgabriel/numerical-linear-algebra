from functions import *

tol = 5*10**-4
niter = 1000

def func1(X):
    return X[0] + 2*X[1] - 2

def func2(X):
    return X[0]**2 + 4*(X[1]**2) -4

X = [2, 3]
funcs = [func1, func2]
print 'X: ' + str(broydenSystem(X, tol, niter, funcs))
