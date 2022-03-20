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
    ref2 = ref.copy()
    ref2 = ref2[::-1]
    c1 = False
    list3 = []
    while c1==False:
        list3.append(ref[-1])
        ref.pop(-1)
        if len(ref) == 0:
            break
        list3.append(ref[0])
        ref.pop(0)
        if len(ref) == 0:
            break
    print(*list3[::-1])
    k1+=1
    if k1==len(list1):
        break
