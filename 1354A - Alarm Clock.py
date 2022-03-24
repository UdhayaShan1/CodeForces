import math
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
    if k1==len(list1):
        break
    ref = list1[k1]
    a = int(ref[0])
    b = int(ref[1])
    c = int(ref[2])
    d = int(ref[3])
    if a <= b:
        print(b)
        k1+=1
        continue
    if d >= c:
        print(-1)
        k1+=1
        continue
    remain = a-b
    print(b + math.ceil(remain/(c-d))*c)
    k1+=1
