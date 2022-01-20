n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
    
k1 = 0
b1 = False
while b1==False:
    points = list1[k1]
    ref = 0
    for i in range(7,1,-1):
        if points>=i:
            ref = i
            break
    if points % ref == 0:
        print(points // ref)
    else:
        count = points//ref
        count+=1
        print(count)
    k1+=1
    if k1==len(list1):
        break
