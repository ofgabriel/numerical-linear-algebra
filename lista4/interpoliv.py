from functions import *
import sys

def interpolinv(x1,x2,x3,tol,niter):
    #Obs.: x1 < x2 < x3.
    x = [10**36]
    x.extend([x1,x2,x3])
    print x
    y =[0,0,0,0]
    for k in range(1, niter):
        y[1]=test(x[1])
        y[2]=test(x[2])
        y[3]=test(x[3])
        print('y: '+str(y))
        xk = (y[2]*y[3]*x[1])/((y[1]-y[2])*(y[1]-y[3])) + (y[1]*y[3]*x[2])/((y[2]-y[1])*(y[2]-y[3])) + (y[1]*y[2]*x[3])/((y[3]-y[1])*(y[3]-y[2]))
        print xk
        tolk = abs(x[k+1]-x[k])
        if tolk < tol:
            print x[k]
            sys.exit()
        else:
            i = y.index(max(y, key=abs))
            print i
            x[i] = xk
            y[i] = test(x[k])
            x.sort()
            print('x: '+str(x))
            y.sort()
    print("Convergencia nao atingida.")

print interpolinv(3,5,10,5*10**(-4),10)