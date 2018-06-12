from functions import *
from math import sin, cos

def funcDif2Y(t, y, difY):
    return -0.2*difY -y + F(t)

def F(t):
    return 2*sin(0.5*t) + sin(t) + cos(1.5*t)

deltaT = 0.1
tI = 0.0
yI = 0
difYI = 0
tF = 100.0

print 'result: ' + str(integral2ndOrder(INTEGRAL_2_METHOD.TAYLOR, funcDif2Y, tI, yI, difYI, deltaT, tF))
print 'result: ' + str(integral2ndOrder(INTEGRAL_2_METHOD.RUNGE_KUTTA_NYSTROM, funcDif2Y, tI, yI, difYI, deltaT, tF))
