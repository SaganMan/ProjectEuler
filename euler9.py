#Project euler problem 9
#Find product of pythogeran triplet such that their sum is 1000

import math
#PythogeranTriplets=""
for c in range(1001,200,-1):
    for a in range(200,1000):
        if c > a:
            x = math.sqrt(((c*c)-(a*a)))
            if int(x) == math.ceil(x):
                #PythogeranTriplets += (str(int(x)) + "," + str(a) + "," + str(c) + "\n")
                if int(x) + c + a ==1000:
                    print(int(x),c,a)
                    print(int(x)*c*a)
                    break
