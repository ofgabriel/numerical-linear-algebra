import functions as fn

def bissec(a,b,tol):
    #Returns the root of a function given an interval [a,b] and a tol.
    while abs(b-a) > tol:
        x = float(a+b)/2
        f = fn.bis(x)
        if f > 0.0:
            b = x
        else:
            a = x
    return x

print bissec(0,10,0.0001)