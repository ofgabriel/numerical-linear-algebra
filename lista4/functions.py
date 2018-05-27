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

def dif(fun,x):
    y = fun(x)
    dx = 1**-10
    dy = fun(x+dx)
    return (dy - y)/dx

# func   : function that receives an array of params
# X      : array of params
# xIndex : index of the parameter of the derivative
def partDerivative(func, X, xIndex):
    dx = 1**-10
    y1 = func(X)
    X[xIndex] += dx
    y2 = func(X)
    X[xIndex] -= dx # keeps X unchanged
    return (y2 - y1)/dx

# creates matrix with m rows, n columns filled with value
def createMatrix(m,n,value):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(value)
    return matrix

# X : vetor of paramentes for X
# funcs : vetor of functions
def jacobianMatrix(funcs, X):
    J = createMatrix(len(funcs), len(X), None)
    for i in range(len(funcs)):
        for j in range(len(X)):
            J[i][j] = partDerivative(funcs[i], X, j)
    return J

def multiMV(A, X):
    # Multiplies the matrix A x X vector.
    n = len(A)
    m = len(A[0])
    Y = [None for i in range(n)]
    for i in range(n):
        sp = 0.0
        for j in range(m):
            sp += A[i][j]*X[j]
        Y[i] = sp
    return Y

def norma(X):
    return sqrt(sum([x**2 for x in X]))

def subtractVetors(A, B):
    if(len(A) != len(B)):
        print "Subtracting vectors of different size"
        sys.exit()
    return [A[i]-B[i] for i in range(len(A))]

def sumVetors(A, B):
    if(len(A) != len(B)):
        print "Summing vectors of different size"
        sys.exit()
    return [A[i]+B[i] for i in range(len(A))]

def multVectorScalar(B, x):
    return [B[i]*x for i in range(len(B))]