n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append([])
    for j in range(list1[i]):
        temp = []
        x = input().split()
        for k in x:
            temp.append(int(k))
        list2[i].append(temp)
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1]
    ref = list2[k1]
    flag = 0
    x1 = ref[0][0]
    y1 = ref[0][1]
    if x1 < y1:
        k1+=1
        print("NO")
        continue
    for i in range(1,n):
        x1 = ref[i-1][0]
        y1 = ref[i-1][1]
        x2 = ref[i][0]
        y2 = ref[i][1]
        if x2 < x1 or y2 < y1:
            flag+=1
            break
        if (x2 - x1) < (y2-y1):
            flag+=1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
    k1+=1
