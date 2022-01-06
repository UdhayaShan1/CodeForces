n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_list = list1[k1]
    n = int(ref_list[0])
    k = int(ref_list[1])
    list2 = list(range(1,n+1))
    if n == 1 and k == 1:
        print(0)
        k1+=1
        continue
    elif n == 1 and k == 0:
        print(1)
        print(1)
        k1+=1
        continue
    if k == 1:
        list2.pop(0)
        print(len(list2))
        print(*list2)
        k1+=1
        continue
    if k == 2:
        list2.remove(2)
        print(len(list2))
        print(*list2)
        k1+=1
        continue
    c1 = False
    
    k2 = 1
    if k in list2:
        list2.remove(k)
    
    while c1==False:
        if (k-k2) in list2 and k2 in list2 and (k-k2) != k2:
            list2.remove(k2)
        k2+=1
        if k2 == k:
            break
    
    print(len(list2))
    print(*list2)
    k1+=1
