# Project Euler Problem 3
# Largest Prime Factor of 600851475143

no = 600851475143
primes = []
n = 10000
PrimeFactors = []
numbers = [True for i in range(n + 1)]

def SieveOfEratosthenes(n,numbers):
    p = 2
    while (p * p <= n):
        if (numbers[p] == True):
            for i in range(p * 2, n + 1, p):
                numbers[i] = False
        p += 1

    for p in range(2, n):
        if numbers[p]:
            primes.append(p)

SieveOfEratosthenes(n,numbers)

for i in range(0,len(primes)):
    if not no % primes[i]:
        PrimeFactors.append(primes[i])
        
print(max(PrimeFactors))
