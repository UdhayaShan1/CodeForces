n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(input())
    list2.append(input())
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref_s = list1[k1]
    c = list2[k1]
    if c not in set(ref_s):
        print("NO")
        k1+=1
        continue
    if (len(ref_s) - 1) % 2 != 0:
        print("NO")
        k1+=1
        continue
    index_c = [i for i, x in enumerate(ref_s) if x == c]
    flag = 0
    for i in index_c:
        if ((i+1)-1) % 2 == 0 and (len(ref_s) - (i+1)) % 2 == 0:
            flag+=1
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")
    k1+=1
