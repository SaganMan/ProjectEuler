# Project Euler Problem 9
# Pythagorean triplet for which the sum of numbers is 1000, find the product of those three numbers.

import math
for c in range(1001,200,-1):
    for a in range(200,1000):
        if c > a:
            x = math.sqrt(((c*c) - (a*a)))
            if int(x) == math.ceil(x):
                if int(x) + c + a == 1000:
                    print(int(x),c,a)
                    print(int(x)*c*a)
                    break
