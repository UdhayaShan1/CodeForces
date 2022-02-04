n1 = int(input())
flag = 0
x = input()
for i in x:
    if int(i) == 4 or int(i) == 7:
        flag+=1
if flag < n1:
    print("NO")
else:
    x1 = x[0:int(n1/2)]
    x2 = x[int(n1/2):]
    sum1 = 0
    sum2 = 0
    for i in x1:
        sum1+=int(i)
    for i in x2:
        sum2+=int(i)
    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
