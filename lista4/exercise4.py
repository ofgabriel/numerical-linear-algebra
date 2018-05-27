from functions import *

tol = 5*10**-4
niter = 10000

def func1(C):
    return 2*C[1]**2 + C[0]**2 + 6*C[2]**2 - 1

def func2(C):
    return 8*C[1]**3 + 6*C[1]*(C[0]**2) + 36*C[1]*C[0]*C[2] + 108*C[1]*C[2]**2 - theta1

def func3(C):
    return ( 60*C[1]**4 + 60*(C[1]**2)*(C[0]**2) + 576*(C[1]**2)*C[0]*C[2] + 
    2232*(C[1]**2)*(C[2]**2) + 252*(C[2]**2)*(C[0]**2) + 1296*(C[2]**3)*C[0] + 
    3348*(C[2]**4) + 24*(C[0]**3)*C[2] + 3*C[0] - theta2 )

C = [1, 2, 3]
funcs = [func1, func2, func3]
theta1 = 0.0
theta2 = 3.0
print 'Theta1 = 0.0, Theta2 = 3.0'
print 'Newton result: ' + str(newtonSystem(C, tol, niter, funcs))
print 'Broyden result: ' + str(broydenSystem(C, tol, niter, funcs))

theta1 = 0.75
theta2 = 6.5
print 'Theta1 = 0.75, Theta2 = 6.5'
print 'Newton result: ' + str(newtonSystem(C, tol, niter, funcs))
print 'Broyden result: ' + str(broydenSystem(C, tol, niter, funcs))

theta1 = 0.0
theta2 = 11.667
print 'Theta1 = 0.0, Theta2 = 11.667'
print 'Newton result: ' + str(newtonSystem(C, tol, niter, funcs))
print 'Broyden result: ' + str(broydenSystem(C, tol, niter, funcs))
