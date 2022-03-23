n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(input().split())
 
k1 = 0
b1 = False
while b1==False:
    if k1==len(list1):
        break
    ref = list1[k1]
    a1 = int(ref[0])
    k = int(ref[1])
    if k == 1:
        print(a1)
        k1+=1
        continue
    c1 = False
    count = 1
    while c1==False:
        a2 = a1 + int(max(list(str(a1))))*int(min(list(str(a1))))
        if a2 == a1:
            break
        a1 = a2
        count += 1
        if count == k:
            break
        if min(list(str(a1))) == 0:
            break
    print(a1)
    k1+=1
