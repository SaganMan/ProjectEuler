"""
Project Euler Problem 5
To find 10001th prime number
"""

def FindPrime(limit,prime):
    d = 2
    while d*d < limit:
        if prime[d] == True:
            for i in range(d * 2, limit + 1, d):
                prime[i] = False
        d=d+1

    count=0
    for i in range(0,limit):
        if prime[i] == True:
            #print(i)
            count += 1
            if count == 10001:
                print(count,"th prime",i)
                break

limit = 200000
prime = [True for i in range(0, limit+1)]
prime[0] = prime[1] = False
FindPrime(limit,prime)
