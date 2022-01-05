n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))
    
min1 = int(100000000000000000000000000)
temp = []
for i in range(len(list1)-1):
    y = abs(list1[i+1]- list1[i])
    if y < min1:
        temp = []
        min1 = y
        temp.append(i)
        temp.append(i+1)

if abs(list1[-1]- list1[0]) <= min1:
    print(1,len(list1))
else:
    print(temp[0]+1,temp[1]+1)
