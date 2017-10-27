# Project Euler Problem 4
# Largest Palindrome from product of two 3-digit numbers

def palin(n,p):
    s = str(n)
    l = len(s)-1
    i = 0
    flag = 1
    while (i < len(s)) and (l >= 0):
        if s[i]!=s[l]:
            flag = 0
        i += 1
        l -= 1

    if flag == 1:
        p.append(n)

n=0
m=999
p=[]

while m >= 100:
    for i in range(100,(m+1)):
        n = i*m
        palin(n,p)
    m = m - 1

print(max(p))
