n1 = int(input())
list1 = []
list2 = []
list3 = []
for i in range(n1):
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

k3 = 0
b1 = False
while b1==False:
    n = list1[k3][0]
    k1 = list1[k3][1]
    k2 = list1[k3][2]
    ref1 = list2[k3]
    ref2 = list3[k3]
    if n in ref1:
        print("YES")
    else:
        print("NO")
    k3+=1
    if k3==len(list1):
        break
