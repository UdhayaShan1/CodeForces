n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    list1.append(int(input()))
    x = input().split()
    temp = []
    dict1 = {}
    for j in x:
        temp.append(int(j))
        if int(j) not in dict1:
            dict1[int(j)] = 1
        else:
            dict1[int(j)] += 1
    list2.append(dict1)
    list3.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    ref = list2[k1]
    ref_og = list3[k1]
    max1 = 10000000000
    for i in ref.keys():
        if ref[i] >= 2:
            continue
        if i < max1:
            max1 = i
    if max1 == 10000000000:
        max1 = -1
    if max1 != -1:
        print([i for i, x in enumerate(ref_og) if x == max1][0]+1)
    else:
        print(-1)
    k1+=1
    if k1==len(list2):
        break
