import math
n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    n = ref[0]
    k = ref[1]
    if k % n == 0:
        print(k//n)
        k1+=1
        continue
    if n > k:
        k = math.ceil(n/k) * k
        if k % n == 0:
            print(k//n)
        else:
            print(math.floor(k/n)+1)
    else:
        print(math.floor(k/n)+1)
    k1+=1
