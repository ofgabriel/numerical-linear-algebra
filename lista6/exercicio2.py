from functions import *
from math import sin, cos
import matplotlib.pyplot as plt

def funcDif2Y(t, y, difY):
    return -0.2*difY -y + F(t)

def F(t):
    return 2*sin(0.5*t) + sin(t) + cos(1.5*t)

deltaT = 0.1
tI = 0.0
yI = 0
difYI = 0
tF = 100

pts = [(yI + deltaT*i) for i in range(0, int(1 + (tF-tI)/deltaT))]

taylor = derivate2ndOrderTaylor(funcDif2Y, tI, yI, difYI, deltaT, tF)
rkn = rungeKuttaNystrom(funcDif2Y, tI, yI, difYI, deltaT, tF)

plt.figure(1)
plt.plot(pts,taylor,'ro')
plt.ylabel('Taylor')
plt.figure(2)
plt.plot(pts,rkn,'ro')
plt.ylabel('Runge Kutta Nystrom')
plt.show()

file = open('exercicio2.txt', 'w')
file.write('Pontos' + ' ' + 'Taylor' + ' ' + 'RKN' + '\n')
for i in range(len(pts)):
    file.write(str(pts[i]) + ' ' + str(taylor[i]) + ' ' + str(rkn[i]) + '\n')
file.close()
