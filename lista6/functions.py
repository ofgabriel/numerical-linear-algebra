from math import *
import sys
sys.path.append('../lista1/')
from DecomposicaoLU import resolveSystem
sys.path.append('../lista2/')
from mathMethods import multiMM, multiMS

def euler(funcDifX, deltaT, tI, funcTIResult, tF):
    NITER = 1 + (tF-tI)/deltaT
    if NITER != int(NITER):
        print 'Exception: supposed to be integer'
        sys.exit()
    NITER = int(NITER)

    funcResults = [None for i in range(NITER)]
    funcResults[0] = funcTIResult

    for i in range(1, NITER):
        t = tI + (i-1)*deltaT
        funcResults[i] = funcResults[i-1] + funcDifX(t, funcResults[i-1]) * deltaT
    return funcResults

def integral(funcDifX, deltaT, tI, funcTIResult, tF):
    derivateResults = euler(funcDifX, deltaT, tI, funcTIResult, tF)
    print derivateResults
    return derivateResults[-1] - derivateResults[0]
