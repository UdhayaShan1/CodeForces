n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    list2.append(input())
    
k1 = 0
b1 = False
while b1==False:
    if k1 ==len(list1):
        break
    n = list1[k1]
    s = list2[k1]
    list_first = []
    for i in range(n):
        if s[i] == "8":
            list_first.append(i)
            break
    if len(list_first) == 0:
        k1+=1
        print("NO")
        continue
    if n - list_first[0] >= 11:
        print("YES")
    else:
        print("NO")
    k1+=1
