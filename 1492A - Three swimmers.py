import math
from decimal import *
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
    ref_list = list1[k1]
    p = ref_list[0]
    list2 = ref_list[1:]
    min1 = 0
    k2 = 0
    c1 = False
    while c1==False:
        if k2==len(list2):
            print(min1)
            k1+=1
            break
        ref = list2[k2]
        if p > ref:
            result = math.ceil(Decimal(p)/Decimal(ref))*ref - p
            if k2==0:
                min1 = result
            if result < min1 and k2!=0:
                min1 = result
            k2+=1
        else:
            if k2==0:
                min1 = abs(p-ref)
            if abs(p-ref) < min1 and k2!=0:
                min1 = abs(p-ref)
            k2+=1

        
