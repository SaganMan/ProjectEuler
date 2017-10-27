# Project Euler Problem 2
# Sum of even fibonacci numbers less than four million

import numpy
fibonaci = [1,2]
x = 0

while numpy.amax(fibonaci) < 4000000:
    if (fibonaci[x] + fibonaci[x+1]) > 4000000:
        break
    fibonaci.append(fibonaci[x] + fibonaci[x+1])
    x = x+1

l = len(fibonaci)

while l > 0:
    if fibonaci[l-2]%2 != 0:
        fibonaci.pop(l-2)
    l -= 1

print(sum(fibonaci))
