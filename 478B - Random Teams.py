from math import comb
x = input().split()
n = int(x[0])
m = int(x[1])
max1 = comb(n-(m-1),2)
if n == m:
    print(0,0)
elif n % m == 0:
    print(comb(n//m,2)*m,max1)
else:
    start = n//m
    no_start = m
    remainder = n % m
    no_second = remainder
    no_start -= remainder
    try1 = comb(start,2) * no_start + comb(start+1,2)*no_second
    print(try1,max1)
