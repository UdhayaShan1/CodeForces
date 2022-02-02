n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    count = 0
    list2 = []
    for i in range(int((4*n)/2),4*n+1,2):
        list2.append(i)
        count+=1
        if count>=n:
            break
    print(*list2)
    k1+=1
    if k1==len(list1):
        break
