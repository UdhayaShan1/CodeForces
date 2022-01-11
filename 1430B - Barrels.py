n1 = int(input())
list1 = []
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
    
k1 = 0
b1 = False
while b1==False:
    ref_list1 = list1[k1]
    n = ref_list1[0]
    k = ref_list1[1]
    ref_list2 = list2[k1]
    ref_list2.sort()
    ref_list2.reverse()
    c1 = False
    count = 0
    k2 = 1
    while c1==False:
        if count == k:
            break
        temp1 = ref_list2[0]
        temp2 = ref_list2[k2]
        ref_list2[0]  = temp1+temp2
        k2+=1
        count+=1
    print(ref_list2[0])
    k1+=1
    if k1==len(list2):
        break
