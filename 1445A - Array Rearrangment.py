n1 = int(input())
list1 = []
list2 = []
list3 = []
count = 0
for i in range(n1):
    count+=1
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
    if count < n1:
        x = input()
        
k1 = 0
b1 = False
while b1==False:
    ref_list1 = list1[k1]
    n = ref_list1[0]
    x = ref_list1[1]
    ref_list2 = list2[k1]
    ref_list3 = list3[k1]
    ref_list2.sort()
    ref_list3.sort()
    ref_list3.reverse()
    flag = 0 
    k2 = 0
    c1 = False
    while c1==False:
        if ref_list2[k2]+ref_list3[k2] > x:
            flag+=1
            break
        k2+=1
        if k2==len(ref_list3):
            break
    if flag>0:
        print("No")
    else:
        print("Yes")
    k1+=1
    if k1==len(list1):
        break
