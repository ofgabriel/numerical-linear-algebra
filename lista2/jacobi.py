def getMaxAbsItemOutDiagonal(A):
    maxItem = (0, 1)  # random initial max item
    n = len(A)
    for i in range(n):
        for j in range(n):
            if(i != j):  # excludes elements of diagonal
                if(abs(A[i][j]) > abs(A[maxItem[0]][maxItem[1]])):
                    maxItem = (i, j)
    return maxItem
