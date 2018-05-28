from functions import *
from math import exp

tol = 5*10**-4
niter = 1000

def func1(B):
    return B[0] + B[1]*(1**B[2]) - 1

def func2(B):
    return B[0] + B[1]*(2**B[2]) - 2

def func3(B):
    return B[0] + B[1]*(3**B[2]) - 9

X = [1, 1, 1]
funcs = [func1, func2, func3]
print 'Mínimos quadrados NL result: ' + str(leastSquareNL(X, tol, niter, funcs))
