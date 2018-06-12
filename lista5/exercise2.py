from functions import *
import numpy as m

def ex2(x):
    y = (1/(m.sqrt(2*m.pi)))*m.exp(-1/2*x**2)
    return y

# def teste(x):
#     return x**2

# def example(x):
#     return 2 + x + 2*x**2

print quadratura(ex2,0,1,2)

print polinomial(ex2,0,1,2)