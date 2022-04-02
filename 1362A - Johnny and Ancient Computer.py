import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0 
b1 = False
while b1==False:
    ref = list1[k1]
    a = int(ref[0])
    b = int(ref[1])
    max1 = max(a,b)
    min1 = min(a,b)
    if max1 % min1 != 0:
        print(-1)
    else:
        diff = max1 // min1
        flag = -1
        power = 0
        for i in range(0,1000):
            if (2**i) == diff:
                flag = 1
                power = i
                break
        if flag == 1:
            x = power
            check = [3,2,1]
            count = 0
            for i in check:
                count += x // i
                x = x % i
            print(int(count))
        else:
            print(-1)
    k1+=1
    if k1==len(list1):
        break
