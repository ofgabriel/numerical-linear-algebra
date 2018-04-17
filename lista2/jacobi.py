import math
import numpy as np
import mathMethods


def jacobi(A):
    X = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    toleranceThreshold = 0.001

    maxItem = getMaxItem(A)
    while A[maxItem[0]][maxItem[1]] > toleranceThreshold:  # while not diagonal
        maxItem = getMaxItem(A)
        print np.matrix(A)
        print np.matrix(makePMatrix(A, maxItem))
        break


def getMaxItem(A):
    """get max absolute item outside
    diagonal from a simetric matrix"""

    maxItem = (1, 0)  # random initial max item
    n = len(A)
    for i in range(n):
        for j in range(i):
            if(abs(A[i][j]) > abs(A[maxItem[0]][maxItem[1]])):
                maxItem = (i, j)
    return maxItem


def getPhi(A, maxItem):
    i, j = maxItem
    if(A[i][i] == A[j][j]):
        return math.pi
    else:
        return math.atan(2*A[i][j] / (A[i][i] - A[j][j]))/2


def makePMatrix(A, maxItem):
    n = len(A)
    P = [[0.0 for i in range(n)] for j in range(n)]

    # fills diagonal
    for i in range(n):
        P[i][i] = 1

    # fills the rotation
    i, j = maxItem
    phi = getPhi(A, maxItem)
    P[i][i] = math.cos(phi)
    P[j][j] = math.cos(phi)
    P[i][j] = math.sin(phi)
    P[j][i] = -math.sin(phi)

    return P


testeReal = [[1.0, 0.2, 0.0], [0.2, 1.0, 0.5], [0.0, 0.5, 1.0]]
print jacobi(testeReal)
