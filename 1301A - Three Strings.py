n1 = int(input())
list1 = []
for i in range(n1):
    list1.append([])
    list1[i].append(input())
    list1[i].append(input())
    list1[i].append(input())
    
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    a = list1[k1][0]
    b = list1[k1][1]
    c = list1[k1][-1]
    count = 0
    c1 = False
    k2 = 0
    while c1==False:
        if k2==len(a):
            print("YES")
            break
        if a[k2] == b[k2] and a[k2] != c[k2]:
            print("NO")
            break
        elif a[k2] == b[k2] and a[k2] == c[k2]:
            count+=1
            k2+=1
            continue
        elif a[k2] != b[k2]:
            if a[k2] == c[k2] or b[k2] == c[k2]:
                count+=1
                k2+=1
                continue
            else:
                print("NO")
                break
    k1+=1
    continue
