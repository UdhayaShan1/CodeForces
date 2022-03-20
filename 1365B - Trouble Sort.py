n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
    list1.append(int(input()))
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

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    n = list1[k1]
    ref1 = list2[k1]
    ref2 = list3[k1]
    ref3 = ref1.copy()
    ref3.sort()
    if ref1 == ref3:
        print("Yes")
        k1+=1
        continue
    if len(set(ref2)) == 2:
        print("Yes")
    else:
        print("No")
    k1+=1
