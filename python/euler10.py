# Project euler Problem 10
# Sum of all primes below two million

primes = [True for x in range(2000001)]
p = 2
while p*p <= 2000000:
    if primes[p]:
        for x in range(2*p, 2000001, p):
            primes[x] = False
    p += 1

p = 0

for x in range(2, 2000000):
    if primes[x]:
        p += x

print(p)
