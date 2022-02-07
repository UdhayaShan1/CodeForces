x = input().split()
n = int(x[0])
a = int(x[1])
b = int(x[2])
list1 = []
list2 = []
x = input().split()
for i in x:
    list1.append(int(i))
x = input().split()
for i in x:
    list2.append(int(i))
list3 = [0]*n
temp = []
common = []

for i in list1:
    if i in list2:
        common.append(i)
    else:
        list3[i-1] = 1
for i in list2:
    if i not in common:
        list3[i-1] = 2

for i in common:
    list3[i-1] = 1

print(*list3)
