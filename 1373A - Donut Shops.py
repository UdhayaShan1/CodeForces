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
    a = int(ref[0])
    b = int(ref[1])
    c = int(ref[2])
    if (c/b) >= a:
        print(1,-1)
        k1+=1
        continue
    if a >= c:
        print(-1,b)
        k1+=1
        continue
    print(1,b)
    k1+=1
