import math
n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    a = int(ref[0])
    b = int(ref[1])
    diff = abs(a-b)
    if diff == 0:
        print(0,0)
    else:
        min1 = min(a,b)
        try1 = min1 - math.floor(min1/diff)*diff
        try2 = math.ceil(min1/diff)*diff - min1
        if try1 < 0:
            try1 = 100000000000
        if try2 < 0:
            try2 = 100000000000
        print(diff,min(try1,try2))
        
    k1+=1
