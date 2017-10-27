# Project Euler Problem 4
# To find smallest multiple of numbers from 1 to 20

def factr(n):
    d = 2
    f1 = []
    while d*d <= n:
        while n%d == 0:
            f1.append(d)
            n //= d
        d += 1
    if n > 1:
        f1.append(n)
    return f1

f=[]
n=[2,3,5,7,11,13,17,19]
m=[0 for i in range(0,21)]
mx=21

for i in range(2,mx):
    f = factr(i)
    for k in range(0,8):
        if f.count(n[k]) > m[n[k]]:
            m[n[k]] = f.count(n[k])

s=1
for j in range(0,mx):
    if m[j] != 0:
        s = s* (j ** m[j])
print(s, "smallest multiple of numbers in range 1 to",mx-1)
