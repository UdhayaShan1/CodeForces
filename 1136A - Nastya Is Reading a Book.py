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
    n = list1[k1]
    ref_list = list2[k1]
    count = 1
    c1 = False
    sort = ref_list.copy()
    sort.sort()
    while c1==False:
        if ref_list == sort:
            print(count-1)
            break
        if count % 2 != 0:
            for i in range(len(ref_list)-1):
                temp = ref_list[i]
                temp1 = ref_list[i+1]
                if i % 2 == 0:
                    if ref_list[i] > ref_list[i+1]:
                        ref_list[i] = temp1
                        ref_list[i+1] = temp
        else:
            for i in range(len(ref_list)-1):
                temp = ref_list[i]
                temp1 = ref_list[i+1]
                if i % 2 != 0:
                    if ref_list[i] > ref_list[i+1]:
                        ref_list[i] = temp1
                        ref_list[i+1] = temp
        count+=1
    k1+=1
    if k1==len(list2):
        break
