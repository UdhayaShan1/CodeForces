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
    
k5 = 0
b1 = False
while b1==False:
    if k5==len(list2):
        break
    ref_list1 = list1[k5]
    ref_list2 = list2[k5]
    n = ref_list1[0]
    k1 = ref_list1[1]
    k2 = ref_list1[2]
    w = ref_list2[0]
    b = ref_list2[1]
    if (w+b) == 0:
        print("YES")
        k5+=1
        continue
    if (k2+k1) == 1 and n == 1:
        print("NO")
        k5+=1
        continue
    
    white_to_make = min(k1,k2)
    white_to_make = white_to_make + (max(k1,k2)-min(k1,k2)) // 2
    black_to_make = (max(k1,k2)-min(k1,k2)) // 2
    black_to_make +=  n - max(k1,k2)
    if w <= white_to_make and b <= black_to_make:
        print("YES")
    else:
        print("NO")
    k5+=1
    
