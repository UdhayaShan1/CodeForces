from decimal import *
n1 = int(input())
sum1 = (Decimal(n1)/2 * Decimal(n1+1))
if sum1 % 2 == 0:
    print(0)
else:
    print(1)
