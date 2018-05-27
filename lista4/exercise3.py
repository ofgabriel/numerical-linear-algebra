from functions import *

tol = 5*10**-4
niter = 1000

def func1Lista(X):
    return 16*(X[0]**4) + 16*(X[1]**4) + (X[2]**4) - 16

def func2Lista(X):
    return X[0]**2 + X[1]**2 + X[2]**2 - 3

def func3Lista(X):
    return X[0]**3 - X[1] + X[2] - 1

X = [1, 2, 3]
funcsLista = [func1Lista, func2Lista, func3Lista]
print 'Newton result: ' + str(newtonSystem(X, tol, niter, funcsLista))
print 'Broyden result: ' + str(broydenSystem(X, tol, niter, funcsLista))