n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
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
    ref_list.sort()
    ref_1 = ref_list[0:n]
    ref_2 = ref_list[n:]
    list3 = [-1]*2*n
    for i in range(len(list3)):
        if i % 2 == 0:
            list3[i] = ref_2[0]
            ref_2.pop(0)
        else:
            list3[i] = ref_1[0]
            ref_1.pop(0)
    print(*list3)
    k1+=1
    if k1==len(list1):
        break
