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
    ref.sort()
    list3 = list(set(ref))
    list3.sort()
    ref2 = ref.copy()
    for i in list3:
        ref2.remove(i)
    ref2.sort()
    list3 += ref2
    print(*list3)
    k1+=1
    if k1==len(list1):
        break
