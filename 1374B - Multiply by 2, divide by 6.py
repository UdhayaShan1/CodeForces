n1= int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

k1 = 0
b1 = False
while b1==False:
    ref = list1[k1]
    c1 = False
    count = 0
    while c1==False:
        if ref == 1:
            print(count)
            break
        if ref % 6 == 0:
            ref = ref // 6
            count+=1
        else:
            ref = ref * 2
            if ref % 6 != 0:
                print(-1)
                break
            count+=1
    k1+=1
    if k1==len(list1):
        break
