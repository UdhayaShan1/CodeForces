n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    list2 = []
    for i in range(1,ref+1):
        list2.append(i)
    for i in range(0,len(list2)-1,2):
        temp1 = list2[i]
        temp2 = list2[i+1]
        list2[i] = temp2
        list2[i+1] = temp1
    if ref % 2 != 0:
        temp1 = list2[-2]
        temp2 = list2[-1]
        list2[-2] = temp2
        list2[-1] = temp1
    print(*list2)
    k1+=1
    if k1==len(list1):
        break
