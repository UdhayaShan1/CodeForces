import math
n1 = int(input())
list3 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list3.append(temp)
    
k1 = 0
b1 = False

while b1==False:
    if k1==len(list3):
        break
    ref_list = list3[k1]
    n = ref_list[0]
    k = ref_list[1]
    list1 = []
    max_rooks = math.ceil(n/2)
    if k > max_rooks:
        print(-1)
        k1+=1
        continue
    for i in range(n):
        list1.append([])
        for j in range(n):
            list1[i].append(".")
    if k == 1:
        list1[i][0] = "R"
        for i in list1:
            print(''.join(i))
        k1+=1
        continue
    k2 = 0
    rook_count = 0
    for i in range(len(list1)):
        if rook_count == k:
            break
        if i % 2 == 0:
            list1[i][k2] = "R"
            rook_count+=1
            k2+=2
    for i in list1:
        print(''.join(i))
    k1+=1
    continue            
