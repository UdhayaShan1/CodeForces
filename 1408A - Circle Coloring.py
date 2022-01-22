n1 = int(input())
listn = []
list1 = []
list2 = []
list3 = []
for i in range(n1):
    listn.append(int(input()))
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
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list3.append(temp)
    
k1 = 0
b1 = False
while b1==False:
    n = listn[k1]
    str1 = list1[k1]
    str2 = list2[k1]
    str3 = list3[k1]
    temp_list = [(str1[0])]
    k2 = 1
    c1 = False
    while c1==False:
        if k2 == n-1:
            break
        if str1[k2] != temp_list[k2-1]:
            temp_list.append(str1[k2])
        elif str2[k2] != temp_list[k2-1]:
            temp_list.append(str2[k2])
        elif str3[k2] != temp_list[k2-1]:
            temp_list.append(str3[k2])
        k2+=1
    
    if str1[-1] != temp_list[-1] and str1[-1] != temp_list[0]:
        temp_list.append(str1[-1])
    elif str2[-1] != temp_list[-1] and str2[-1] != temp_list[0]:
        temp_list.append(str2[-1])
    elif str3[-1] != temp_list[-1] and str3[-1] != temp_list[0]:
        temp_list.append(str3[-1])
    print(*temp_list)
    k1+=1
    if k1==len(list3):
        break
