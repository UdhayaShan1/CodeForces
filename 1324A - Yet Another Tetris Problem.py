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
    if k1==len(list1):
        break
    n = list1[k1]
    ref = list2[k1]
    if n == 1:
        print("YES")
        k1+=1
        continue
    if len(set(ref)) == 1:
        print("YES")
        k1+=1
        continue
    ref.sort()
    flag = 0
    for i in range(len(ref)):
        for j in range(len(ref)):
            if i == j:
                continue
            if abs(ref[i]-ref[j]) % 2 != 0:
                flag+=1
                break
        if flag == 1:
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
    k1+=1
