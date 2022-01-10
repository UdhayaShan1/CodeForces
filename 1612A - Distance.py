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
    ref_list = list1[k1]
    x = ref_list[0]
    y = ref_list[1]
    if (x+y) % 2 != 0:
        print(-1,-1)
        k1+=1
        continue
    if x>=y:
        dist = int((x+y)/2)
        tempx = dist-y
        tempy = y
        c1 = False
        while c1==False:
            if tempy < 0:
                break
            if abs(tempx - x) + abs(tempy - y) == dist:
                print(tempx,tempy)
                break
            tempy-=1
            tempx+=1
    elif x < y:
        dist = int((x+y)/2)
        tempx = x
        tempy = dist-x
        c1 = False
        while c1==False:
            if tempx < 0:
                break
            if abs(tempx - x) + abs(tempy - y) == dist:
                print(tempx,tempy)
                break
            tempy+=1
            tempx-=1
    k1+=1
