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
    ref_list2 = list2[k1]
    n = ref_list1[0]
    k = ref_list1[1]
    c1 = False
    count = 0
    for_once = 0
    min1 = min(ref_list2)
    for i in ref_list2:
        if min1 == i:
            if for_once == 0:
                for_once+=1
                continue
            else:
                count += (k-i) // min1
        else:
            count += (k-i) // min1
    print(count)
    k1+=1
    if k1==len(list2):
        break
