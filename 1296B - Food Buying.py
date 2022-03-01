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
    if ref < 10:
        print(ref)
        k1+=1
        continue
    c1 = False
    count = 0
    while c1==False:
        count += (ref//10) * 10
        ref = ref % 10 + (ref//10)
        if ref < 10:
            count += ref
            break
    print(count)
    k1+=1
