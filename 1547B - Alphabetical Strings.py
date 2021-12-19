n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input())
alpha = list("abcdefghijklmnopqrstuvwxyz")
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_str = list1[k1]
    list2 = []
    temp_str = list(ref_str).copy()
    temp_str.sort()
    indices_last = [i for i, x in enumerate(alpha) if x == temp_str[-1]][0]
    alpha2 = alpha[:indices_last+1]
    break_no = 0
    break_yes = 0
    check_all_inside = 0
    
    for i in alpha2:
        if i in list(ref_str):
            check_all_inside+=1
    if check_all_inside != len(alpha2) or len(alpha2) != len(ref_str):
        print("NO")
        k1+=1
        continue
    for i in alpha2:
        indices = [j for j, x in enumerate(ref_str) if x == i]
        if i == 'a':
            list2.append(indices[0])
        else:
            if indices[0] > list2[-1] and abs(indices[0]-list2[-1]) ==1:
                list2.append(indices[0])
            elif indices[0] < list2[0] and abs(indices[0]-list2[0]) ==1:
                list2.insert(0,indices[0])
            else:
                break_no+=1
                break
    if break_no>=1:
        print("NO")
        k1+=1
        continue
    else:
        print("YES")
        k1+=1
        continue
        
    
