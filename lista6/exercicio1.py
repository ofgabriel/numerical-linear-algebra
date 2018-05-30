from functions import *

def funcDifY(t, funcY):
    return -2*t*(funcY**2)

def funcYExata(t):
    return 1.0/(1+(t**2))

tI = 0
funcTIResult = 1
tF = 2

print 'result: ' + str(integral(INTEGRAL_METHOD.EULER, funcDifY, 0.0001, tI, funcTIResult, tF))
print 'result: ' + str(integral(INTEGRAL_METHOD.RUNGE_KUTTA_2, funcDifY, 0.01, tI, funcTIResult, tF))
print 'result: ' + str(integral(INTEGRAL_METHOD.RUNGE_KUTTA_4, funcDifY, 0.1, tI, funcTIResult, tF))
print 'result: ' + str(funcYExata(tF) - funcYExata(tI))
