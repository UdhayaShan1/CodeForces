x = input().split()
n = int(x[0])
m = int(x[1])

b1 = False
start = 1
if n < m:
    print(-1)
else:
    while b1==False:
        if (2*(m*start)) - n >= 0:
            break
        start+=1
    print(m*start)
