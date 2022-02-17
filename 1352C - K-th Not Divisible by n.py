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
    n = list1[k1][0]
    k = list1[k1][1]
    diff = n-1
    ref = n + ((k//diff)-1)*(n)
    if k%diff == 0:
        print(ref-1)
    else:
        print(ref + k%diff)
    k1+=1
    if k1==len(list1):
        break
