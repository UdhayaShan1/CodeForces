n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1.append(temp)
positive = 0
negative = 0
for i in list1:
    if i[0] > 0:
        positive+=1
    elif i[0] < 0:
        negative+=1
if negative <= 1 and positive>0:
    print("Yes")
elif negative > 0 and positive <=1:
    print("Yes")
else:
    print("No")
