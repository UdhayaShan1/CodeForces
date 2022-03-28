n1 = int(input())
list1 = []
for i in range(n1):
    x = (input().split())
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
    r = int(ref[0])
    g = int(ref[1])
    b = int(ref[2])
    w = int(ref[3])
    c1 = False
    while c1==False:
        flag = 0
        odd = 0
        even = 0
        for i in ref:
            if int(i) % 2 == 0:
                even+=1
            else:
                odd+=1
        if odd == 1 and even > 0:
            flag+=1
            break
        if odd == 0 and even > 0:
            flag+=1
            break
        breakliao = 0
        for i in range(len(ref)-1):
            ref[i] -= 1
            if ref[i] < 0:
                breakliao+=1
                break
        if breakliao > 0:
            break
        ref[-1] += len(ref)-1
        flag = 0
        odd = 0
        even = 0
        for i in ref:
            if int(i) % 2 == 0:
                even+=1
            else:
                odd+=1
        if odd == 1 and even > 0:
            flag+=1
            break
        if odd == 0 and even > 0:
            flag+=1
            break
        break
        
 
    if flag == 1:
        print("Yes")
    else:
        print("No")
    k1+=1
