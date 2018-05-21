from functions import *
import sys

def secante(x0,tol,niter):
    dx = 0.001
    x = []
    x.extend([x0,x0+dx])
    fa = two(x[0])
    for k in range(1,niter):
        fi = two(x[k])
        xk = x[k] - fi*(x[k]-x[k-1])/(fi-fa)
        x.append(xk)
        tolk = abs(x[k+1]-x[k])
        print x
        if tolk < tol:
            print('Raiz: ' + str(x[k]))
            sys.exit()
        else:
            fa = fi
    print('Convergencia nao atingida.')

print secante(-2,5*10**-4,10)