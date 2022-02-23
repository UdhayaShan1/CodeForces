n1 = int(input())
if n1 % 2 != 0:
    print(-1)
else:
    list1 = []
    for i in range(1,n1+1):
        list1.append(i)
    b1 = False
    k2 = 1
    while b1==False:
        temp1 = list1[k2-1]
        temp2 = list1[k2]
        list1[k2-1] = temp2
        list1[k2] = temp1
        k2+=2
        if k2>=n1:
            break
    print(*list1)
