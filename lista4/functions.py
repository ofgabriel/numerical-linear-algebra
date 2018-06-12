#Functions archive:
from math import *
import sys
sys.path.append('../lista1/')
from DecomposicaoLU import resolveSystem
sys.path.append('../lista2/')
from mathMethods import multiMM, multiMS

def test(x):
    return (x**2 - 4*cos(x))

def one(x):
    part = cosh(x*sqrt(9.806*0.00341))
    return log10(part)-50
    #Bissection: for the interval [600,700] and tol = .0001, the root is 633.387470245.
    #Secante: for x0 = 650, tol = 5x10^-4 and niter = 10, the root is 633.387419103.
    #Newton: for x0 = 650, tol = 5x10^-4 and niter = 10, the root is 633.387419103.

def two(x):
    return 4*cos(x) - exp(2*x)
    #Bissection: for the interval [-2,-1] and tol = .0001, the root is -1.55975341797.
    #Newton: for x0 = -2, tol = 5x10^-4 and niter = 10, the root is -1.55966887236.
    #Secante: for x0 = -2, tol = 5x10^-4 and niter = 10, the root is -1.55975081185.
    #In fact, there are multiples roots and the result depends on the x0 defined.

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

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def vector2matrix(A):
    return [[A[i]] for i in range(len(A))]

def sumMatrix(A, B):
    if(len(A) != len(B)) or (len(A[0]) != len(B[0])):
        print "Summing matrices of different sizes"
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def broydenSystem(X, tol, niter, funcs):
    J = jacobianMatrix(funcs, X)
    #print 'J: ' + str(J)
    B = J
    F = [func(X) for func in funcs]
    interacoes = 0
    for k in range(niter):
        deltaX = resolveSystem(B, F)
        deltaX = multVectorScalar(deltaX, -1)
        X = sumVetors(X, deltaX)
        diff = norma(deltaX)/norma(X)
        iteracoes += 1
        if(diff < tol):
            return('Vetor solucao: ' + str(X) + '\nNumero de iteracoes: ' + str(iteracoes)) + '\n'
        else:
            F2 = [func(X) for func in funcs]
            Y = subtractVetors(F2, F)
            F = F2

            # calculates next B
            term1 = subtractVetors(Y, multiMV(B, deltaX))
            term2 = multiMM(vector2matrix(term1), transpose(vector2matrix(deltaX)))
            term3 = 1/multiMV(transpose(vector2matrix(X)), X)[0]
            term4 = multiMS(term2, term3)
            B = sumMatrix(B, term4)
    print("Convergencia nao atingida.")

# funcs : vetor of functions
# X     : vetor of initial values for the funcs params
def newtonSystem(X, tol, niter, funcs):
    iteracoes = 0
    for k in range(niter):
        J = jacobianMatrix(funcs, X)
        #print 'J: ' + str(J)
        F = [func(X) for func in funcs]
        #print 'F: ' + str(F)
        deltaX = resolveSystem(J, F)
        deltaX = multVectorScalar(deltaX, -1)
        #print 'deltaX: ' + str(deltaX)
        X = sumVetors(X, deltaX)
        diff = norma(deltaX)/norma(X)
        iteracoes += 1
        if(diff < tol):
            return('Vetor solucao: ' + str(X) + '\nNumero de iteracoes: ' + str(iteracoes)) + '\n'

    print("Convergencia nao atingida.")

def leastSquareNL(B, tol, niter, funcs):
    for k in range(niter):
        J = jacobianMatrix(funcs, B)
        JTranspose = transpose(J)
        F = [func(B) for func in funcs]
        deltaB = resolveSystem(
            multiMM(JTranspose, J),
            multiMV(JTranspose, F)
        )
        deltaB = multVectorScalar(deltaB, -1)
        #print 'deltaB: ' + str(deltaB)
        B = sumVetors(B, deltaB)
        diff = norma(deltaB)/norma(B)
        if(diff < tol):
            return B

    print("Convergencia nao atingida.")

def bissec(a,b,tol,fun):
    #Returns the root of a function given an interval [a,b] and a tol.
    while abs(b-a) > tol:
        x = float(a+b)/2
        f = fun(x)
        #Replace the number of the function defined in the archive.
        if f > 0.0:
            b = x
        else:
            a = x
    return x

def newton(x,tol,niter,fun):
    for k in range(niter):
        xk = x - fun(x)/dif(fun,x)
        #Replace the function and it's diff defined in the fucntions archive.
        tolk = abs(xk - x)
        x = xk
        if tolk < tol:
            print("Raiz: " + str(xk))
            sys.exit()
    print("Convergencia nao atingida.")
