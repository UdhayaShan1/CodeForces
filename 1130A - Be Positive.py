import math
n1 = int(input())
x = input().split()
list1 = []
pos = 0
neg = 0
for i in x:
    if int(i) > 0:
        pos+=1
    elif int(i) < 0:
        neg+=1
    list1.append(int(i))

ref = math.ceil(n1/2)

if pos>=neg:
    if pos >= ref:
        print(1)
    else:
        print(0)
else:
    if neg >= ref:
        print(-1)
    else:
        print(0)
