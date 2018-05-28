from functions import *
from math import exp

tol = 5*10**-4
niter = 1000

def func1(X):
    return exp((1**X[0])/X[1]) - 1.995

def func2(X):
    return exp((2**X[0])/X[1]) - 1.410

def func3(X):
    return exp((3**X[0])/X[1]) - 1.260

X = [1, 2]
funcs = [func1, func2, func3]
print 'Mínimos quadrados NL result: ' + str(leastSquareNL(X, tol, niter, funcs))
