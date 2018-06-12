from functions import *

def funcDif2X(t, X, difX):
    return (-1)*9.80665 - difX*abs(difX)

deltaT = 0.1
tI = 0.0
xI = 0
difXI = 0
tF = 1.0

print 'result: ' + str(
    integral2ndOrder(
        INTEGRAL_2_METHOD.RUNGE_KUTTA_NYSTROM,
        funcDif2X, tI, xI, difXI, deltaT, tF
    )
)
