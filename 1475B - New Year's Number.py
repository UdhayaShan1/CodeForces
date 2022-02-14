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
    if ref < 2020:
        print("NO")
        k1+=1
        continue
    if ref % 2020 == 0:
        print("YES")
        k1+=1
        continue
    c1 = False
    while c1==False:
        check = ref // 2020
        current1 = ref % 2020
        if current1 <= check:
            print("YES")
            break
        else:
            print("NO")
            break
    k1+=1
