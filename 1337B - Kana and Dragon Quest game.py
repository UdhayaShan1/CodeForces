n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    x = list1[k1][0]
    n = list1[k1][1]
    m = list1[k1][2]
    b1 = False
    while b1==False:
        if n == 0:
            break
        if x <=20:
            break
        x = (x//2 + 10)
        n-=1
    if x <= 10*m:
        print("YES")
    else:
        print("NO")
    k1+=1
    if k1==len(list1):
        break
