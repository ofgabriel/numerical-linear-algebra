from functions import *
import numpy as m

def ex3(w):
    rao = 1/m.sqrt((1-(w)**2)**2+(2*0.05*w)**2)
    return rao**2*2

print quadratura(ex3,0,10,4)

print polinomial(ex3,0,10,4)