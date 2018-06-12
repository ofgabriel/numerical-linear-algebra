from functions import *
import matplotlib.pyplot as plt

def funcDifY(t, funcY):
    return -10*t*funcY**2

deltaT = 0.1
tI = 0.0
yI = 2
tF = 1.0

result = rungeKutta2(funcDifY, deltaT, tI, yI, tF)

pts = [(tI + deltaT*i) for i in range(0, int(1 + (tF-tI)/deltaT))]

print pts 
plt.figure(1)
plt.plot(pts,result,'ro')
plt.ylabel('Runge Kutta')
plt.show() 