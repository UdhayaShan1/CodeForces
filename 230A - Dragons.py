x = input().split()
s = int(x[0])
n = int(x[1])

list1 = []
for i in range(n):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)

b1 = False
while b1==False:
    flag = 0
    for i in list1:
        if s>i[0]:
            s+=i[1]
            list1.remove(i)
            flag+=1
    if flag == 0:
        break
if len(list1) == 0:
    print("YES")
else:
    print("NO")
