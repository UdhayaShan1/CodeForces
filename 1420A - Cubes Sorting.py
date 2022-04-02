n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(int(input()))
    temp = []
    for j in input().split():
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    ref = list2[k1]
    ref2 = ref.copy()
    ref2.sort()
    if ref == ref2:
        print("YES")
    else:
        if ref == ref2[::-1] and len(set(ref)) == n:
            print("NO")
        else:
            print("YES")
            
    k1+=1
    if k1==len(list1):
        break
