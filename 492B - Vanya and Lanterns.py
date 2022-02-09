x = input().split()
n = int(x[0])
l = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()
max1 = 0
for i in range(len(list1)-1):
    if abs(list1[i+1]-list1[i]) / 2 > max1:
        max1 = abs(list1[i+1]-list1[i])/2
if list1[0] != 0:
    if (list1[0]) > max1:
        max1 = (list1[0])
if l - list1[-1]>max1:
    max1 = l-list1[-1]
print(max1)
