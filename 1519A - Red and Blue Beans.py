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
    ref = list1[k1]
    r = ref[0]
    b = ref[1]
    d = ref[2]
    min1 = min(r,b)
    max1 = max(r,b)
    if max1 % min1 == 0:
        if (max1//min1) - (1) <= d:
            print("YES")
        else:
            print("NO")
    else:
        if (max1//min1 + 1) - 1 <= d:
            print("YES")
        else:
            print("NO")
    k1+=1
    if k1==len(list1):
        break
