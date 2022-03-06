import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    n = int(ref[0])
    k = int(ref[1])
    strings = (n*(n-1))//2
 
    terms1 = (-1 + ((1**2) - (4*1*(-2*strings)))**0.5) / 2
    
    terms2 = (-1 + ((1**2) - (4*1*(-2*k)))**0.5) / 2
    first_b = (n-1) - math.ceil(terms2)
 
    list2 = ["a"]*n
    list2[first_b] = "b"
 
    remainder = k - ((math.ceil(terms2)-1)/2) * (2+((math.ceil(terms2)-1)-1))
 
    list2[-int(remainder)] = "b"
    print("".join(list2))
 
    
    k1+=1
    if k1==len(list1):
        break
