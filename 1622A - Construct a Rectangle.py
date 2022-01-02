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
    if k1==len(list1):
        break
    ref_list = list1[k1]
    ref_list.sort()
    if ref_list[0] == ref_list[1]:
        if ref_list[-1] % 2 == 0:
            print("YES")
        else:
            print("NO")
        k1+=1
        continue
    elif ref_list[1] == ref_list[-1]:
        if ref_list[0] % 2 == 0:
            print("YES")
        else:
            print("NO")
        k1+=1
        continue
    if ref_list[0] + ref_list[1] == ref_list[-1]:
        print("YES")
    else:
        print("NO")
    k1+=1
