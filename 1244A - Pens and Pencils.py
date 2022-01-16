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
    a =  ref[0]
    b = ref[1]
    c = ref[2]
    d =  ref[3]
    k = ref[-1] 
    x = math.ceil(a/c)
    y = math.ceil(b/d)
    if x + y > k:
        print(-1)
        k1+=1
        continue
    print(x,y)
    k1+=1
