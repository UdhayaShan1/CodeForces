n1 = int(input())
list1=  []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list2.append(temp)
k1=0
b1=False
while b1==False:
    ref_list1 = list1[k1]
    ref_list2 = list2[k1]
    n = ref_list1[0]
    k = ref_list1[-1]
    count = 0
    c1 = False
    list3 = ref_list2.copy()
    list5 = []
    max1 = max(list3)
    for i in list3:
        list5.append(max1-i)
    max2 = max(list5)
    list6 = []
    if k % 2 != 0:
        print(*list5)
    else:
        for i in list5:
            list6.append(max2-i)
        print(*list6)
    k1+=1
    if k1==len(list2):
        break
