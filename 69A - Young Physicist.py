n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

flag = 0
k1 = 0
b1 = False
while b1==False:
    sum1 = 0
    for i in list1:
        sum1 += i[k1]
    if sum1 != 0:
        flag +=1
        break
    k1+=1
    if k1==3:
        break
if flag > 0:
    print("NO")
else:
    print("YES")
