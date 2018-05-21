#Functions archive:
from math import *

def test(x):
    return (x**2 - 4*cos(x))

def dif_test(x):
    y = test(x)
    dx = 1**-10
    dy = test(x+dx)
    return (dy - y)/dx

def one(x):
    part = cosh(x*sqrt(9.806*0.00341))
    return log10(part)-50
    #Bissection: for the interval [600,700] and tol = .0001, the root is 633.387470245.
    #Secante: for x0 = 650, tol = 5x10^-4 and niter = 10, the root is 633.387419103.
    #Newton: for x0 = 650, tol = 5x10^-4 and niter = 10, the root is 633.387419103.

def dif_one(x):
    y = one(x)
    dx = 1**-10
    dy = one(x+dx)
    return (dy - y)/dx

def two(x):
    return 4*cos(x) - exp(2*x)
    #Bissection: for the interval [-2,-1] and tol = .0001, the root is -1.55975341797.
    #Newton: for x0 = -2, tol = 5x10^-4 and niter = 10, the root is -1.55966887236.
    #Secante: for x0 = -2, tol = 5x10^-4 and niter = 10, the root is -1.55975081185.
    #In fact, there are multiples roots and the result depends on the x0 defined.

def dif_two(x):
    y = two(x)
    dx = 1**-10
    dy = two(x+dx)
    return (dy - y)/dx