#Testing sympy
from sympy import *
x, y, z = symbols('x y z', real = True)
f = log((cosh(x*sqrt(9.806*0.00341))-50),10)
print diff(f,x)