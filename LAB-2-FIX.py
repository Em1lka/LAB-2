from decimal import Decimal
import numpy as np
import time

def CalculateAmount(matrixX, t):
    t = np.power(0.1, t)
    factorial = 1
    n = 1

    tmp_result = 0
    result = 0
    rng = 1
    
    while(abs(rng) > t):
        tmp_result = result
        result += -abs(np.linalg.det(matrixX * (2 * n + 1))) / factorial
        n += 1
        factorial *= (2 * n + 1)
        rng = tmp_result - result
        print(n-1, ':', result, ' ', rng)
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

result = CalculateAmount(matrixX, t)
print('Result: ' + str(result))
print('========================')
print('Program working ' + str(time.time() - startTime) + ' seconds.')