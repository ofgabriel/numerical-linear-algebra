from functions import *
import sys

def newton(x,tol,niter):
    for k in range(niter):
        xk = x - two(x)/dif_two(x)
        #Replace the function and it's diff defined in the fucntions archive.
        tolk = abs(xk - x)
        x = xk
        if tolk < tol:
            print("Raiz: " + str(xk))
            sys.exit()
    print("Convergencia nao atingida.")

print newton(-10,5*10**-4,10)