from functions import *
import math

def func(x):
    return math.e**x - x**2 - 4

print 'Bisseção: ' + str(bissec(0.0,3.0,0.0001,func))
print 'Newton: ' + str(newton(0.0,0.0001, 25,func))
