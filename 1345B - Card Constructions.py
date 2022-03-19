import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    if ref == 1:
        k1+=1
        print(0)
        continue
    count = 0
    b1 = False
    while b1==False:
        if ref == 2:
            count += 1
            break
        if ref < 2:
            break
        n = math.floor((-0.5 + math.sqrt(0.25-4*1.5*(-ref)))/3)
        count += 1
        ref -= (1.5*(n**2)+0.5*n)
    print(int(count))
    k1+=1
