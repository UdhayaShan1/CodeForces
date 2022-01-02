n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    ref_list = list1[k1]
    n = ref_list[0]
    x = ref_list[1]
    a = ref_list[2]
    b = ref_list[3]
    count_swap = 0
    distance = abs(a-b)
    maxdistance = n-1
    c1 = False
    while c1==False:
        if count_swap == x or abs(distance) == maxdistance:
            print(abs(distance))
            break
        count_swap+=1
        distance+=1
    k1+=1
    if k1==len(list1):
        break
