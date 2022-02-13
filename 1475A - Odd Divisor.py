n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    flag = 0
    for i in range(1,100):
        if (2**i) > ref:
            break
        if ref == (2**i):
            flag+=1
            break
    if flag > 0:
        print("NO")
    else:
        print("YES")
    k1+=1
