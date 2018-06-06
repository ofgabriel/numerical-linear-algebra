from quadratura import *
import numpy as m

def i1(x):
    y = (1/(m.sqrt(2*m.pi)))*m.exp(-1/2*x**2)
    return y

print quadratura(i1,0,1,1)