from functions import *

tol = 5*10**-4
niter = 10

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def newtonSystem(X, tol, niter, funcs):
    print jacobianMatrix(funcs, X)
    F = [func(X) for func in funcs]
    print F

def func1(X):
    return X[0] + 2*X[1] - 2

def func2(X):
    return X[0]**2 + 4*(X[1]**2) -4

X = [2, 3]
funcs = [func1, func2]

newtonSystem(X, tol, niter, funcs)
