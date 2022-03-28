import math
n1 = int(input())
list1 = []
list2 = []
for i in range(n1):
    list1.append(input().split())
    temp = []
    for j in input().split():
        temp.append(int(j))
    list2.append(temp)
 
k1 = 0
b1 = False
while b1==False:
    n = int(list1[k1][0])
    x = int(list1[k1][1])
    ref = list2[k1]
    a = math.ceil(sum(ref)/x)
    b = 0
    for i in ref:
        b += math.ceil(i/x)
    print(min(a,b),max(a,b))
    k1+=1
    if k1==len(list1):
        break
