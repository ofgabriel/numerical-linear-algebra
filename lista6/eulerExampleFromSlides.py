from functions import *

def funcDifX(t, funcX):
    return t + funcX

deltaT = 0.1
tI = 0.0
funcTIResult = 0
tF = 1.0

print 'Euler result: ' + str(integral(funcDifX, deltaT, tI, funcTIResult, tF))
