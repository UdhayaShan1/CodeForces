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
    ref = list2[k1]
    c0 = 0
    c1 = 0
    c2 = 0
    for i in ref:
        if i % 3 == 0:
            c0 += 1
        elif i % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    final = (c0+c1+c2) // 3
    list3 = [c0,c1,c2]
    count = 0
    c1 = False
    while c1==False:
        flag = 0
        for i in range(len(list3)):
            if list3[i] > final and i != 2:
                list3[i+1] += (list3[i]-final)
                count += (list3[i]-final)
                list3[i] = final
            elif list3[i] > final and i == 2:
                list3[0] += (list3[i]-final)
                count += (list3[i]-final)
                list3[i] = final
            if list3[i] == final:
                flag+=1
        if flag == 3:
            break
    print(count)
    k1+=1
    if k1==len(list2):
        break
