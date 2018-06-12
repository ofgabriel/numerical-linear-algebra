from functions import *
from math import *

def func1(x):
    return x[0] - x[1] + 2

def func2(x):
    return exp(x[0]) + x[1] - 5

print newtonSystem([1,1],0.001,10,[func1,func2])

print newtonSystem([1,1],0.001,10,[func1,func2])