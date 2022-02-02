n1 = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))
    
k1 = 0
b1 = False
while b1==False:
    n = list1[k1]
    list2 = []
    c1 = False
    count = 0
    start = 2
    while c1==False:
        list2.append(start)
        start+=1
        count+=1
        if count == n:
            break
    print(*list2)
    k1+=1
    if k1==len(list1):
        break
