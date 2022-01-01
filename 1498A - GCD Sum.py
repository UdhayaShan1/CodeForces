import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

b1 = False
k1 = 0
while b1==False:
    if k1==len(list1):
        break  
    c1 = False
    
    ref_int = list1[k1]
    temp1 = ref_int
    while c1==False:
        ref_sum = 0
        for i in str(temp1):
            ref_sum+=int(i)
        if math.gcd(temp1,ref_sum) > 1:
            print(temp1)
            break
        temp1 += 1
    k1+=1
