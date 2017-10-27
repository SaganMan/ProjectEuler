# Project Euler Problem 2
# Sum of even numbers in Fibonacci sequence less than four million 

import numpy
fibonaci=[1,2]
x=0
y=4000000

while numpy.amax(fibonaci)<y:
    if (fibonaci[x] + fibonaci[x+1]) > y:
        break
    fibonaci.append(fibonaci[x] + fibonaci[x+1])
    x=x+1

l=len(fibonaci)

while l>0:
    if fibonaci[l-2]%2 != 0:
        fibonaci.pop(l-2)
    l=l-1

print(sum(fibonaci))
