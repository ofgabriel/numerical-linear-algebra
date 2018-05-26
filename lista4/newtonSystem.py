from functions import *

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def newtonSystem(X, tol, niter, funcs):
    for k in range(niter):
        i = 1

def func1(X):
    return X[0] + 2*X[1] - 2

def func2(X):
    return X[0]**2 + 4*(X[1]**2) -4

X = [2, 3]
funcs = [func1, func2]
print jacobianMatrix(funcs, X)
