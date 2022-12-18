from decimal import Decimal
import numpy as np
import time

def CalculateAmount(matrixX):
    result = Decimal(0)
    x = 0
    n = 1
    for currentN in range(len(matrixX)):
        for currentM in range(len(matrixX[currentN])):
            x = Decimal(matrixX[currentN][currentM])
            result += Decimal(-(abs(x * Decimal(np.math.factorial(2 * n + 1))) / Decimal(np.math.factorial(2 * n + 1))))
            n += 1
    return result

print('   Laboratory work №1   ')
print('Created by Emil Yarullov')
print('========================')
xN = int(input('Input n: '))
xM = int(input('Input m: ')) 
t = int(input('Input t: ')) # Accuracy of calculations of t decimal places.
print('========================')
startTime = time.time()
matrixX = np.random.rand(xN, xM)
rankX = np.linalg.matrix_rank(matrixX)
print('Matrix X:')
print(matrixX)
print('Rank: ' + str(rankX))
print('========================')
result = round(CalculateAmount(matrixX), t)
print('Result: ' + str(result))
print('========================')
print('Program working ' + str(time.time() - startTime) + ' seconds.')