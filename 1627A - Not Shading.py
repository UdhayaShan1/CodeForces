n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
    list2.append([])
    for k in range(int(x[0])):
        list2[i].append(input())
        
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1][0]
    m = list1[k1][1]
    r = list1[k1][2]
    c = list1[k1][3]
    ref_list = list2[k1]
    flag = 0
    for i in ref_list:
        if 'B' in i:
            flag+=1
        else:
            pass
    if flag == 0:
        print(-1)
        k1+=1
        continue
    if ref_list[r-1][c-1] == "B":
        print(0)
        k1+=1
        continue
    b_flag = 0
    for i in ref_list[r-1]:
        if i == "B":
            b_flag+=1
        else:
            pass
    for i in ref_list:
        if i[c-1] == "B":
            b_flag+=1
    if b_flag>0:
        print(1)
    else:
        print(2)
    k1+=1
    continue
