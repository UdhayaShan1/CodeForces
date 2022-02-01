n1 = int(input())
flag = 0
if n1 == 1:
    print(-1)
    flag +=1
a = 2
b = 2
for i in range(2,200):
    if (a*i) > n1:
        break
    if (a*i) * 2 > n1:
        b = a*i
        break
if flag == 0:
    print(b,a)
