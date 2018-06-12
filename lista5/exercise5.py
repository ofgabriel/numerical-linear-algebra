from functions import *
import numpy as m

def func(x):
    return 2 + 2*x - x**2 + 3*x**3

print quadratura(func,0,4,2)

print polinomial(func,0,4,3)