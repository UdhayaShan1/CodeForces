x = input().split()
n = int(x[0])
m = int(x[1])
list1 = []
list2 = []
x = input().split()
temp = []
for j in x:
    temp.append(int(j))
list1.append(temp)

x = input().split()
temp = []
for j in x:
    temp.append(int(j))
list2.append(temp)

final = []

for i in list1[0]:
    if i in list2[0]:
        final.append(i)
        
print(*final)
