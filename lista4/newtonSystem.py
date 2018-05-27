from functions import *

tol = 5*10**-4
niter = 100

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