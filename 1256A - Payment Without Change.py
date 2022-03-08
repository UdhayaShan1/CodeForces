n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    a = int(ref[0])
    b = int(ref[1])
    n = int(ref[2])
    S = int(ref[3])
    min1 = min(a,S//n)
    flag = 0
    for i in range(min1,-1,-1):
        if S - (i*n) <= b:
            flag+=1
            break
        else:
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")
    k1+=1
    if k1==len(list1):
        break
