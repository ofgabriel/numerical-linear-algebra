import math


def jacobi(A):
    X = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    toleranceThreshold = 0.001

    maxItem = getMaxItem(A)
    while A[maxItem[0]][maxItem[1]] > toleranceThreshold:  # while not diagonal
        A[maxItem[0]][maxItem[1]] = 0
        A[maxItem[1]][maxItem[0]] = 0
        print A
        maxItem = getMaxItem(A)


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


testeReal = [[1.0, 0.2, 0.0], [0.2, 1.0, 0.5], [0.0, 0.5, 1.0]]
print jacobi(testeReal)
