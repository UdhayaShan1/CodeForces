n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]**2
    if ref**0.5 == 2:
        print(-1)
        k1+=1
        continue
    list2 = []
    c1 = False
    start = 1
    while c1==False:
        list2.append(start)
        start += 2
        if start > ref:
            break
    d1 = False
    start = 2
    while d1==False:
        if len(list2) >= ref:
            break
        list2.append(start)
        start += 2
        if start > ref:
            break
    count = 0
    list3 = []
    for i in range(int(ref**0.5)):
        list3.append([])
        c1 = False
        temp = 0
        while c1==False:
            if count == ref:
                break
            list3[i].append(list2[count])
            count+=1
            temp+=1
            if temp == ref**0.5:
                break
    for i in list3:
        print(*i)
    k1+=1
