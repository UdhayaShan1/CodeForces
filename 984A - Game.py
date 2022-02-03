import math
n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()

print(list1[math.ceil(n1/2)-1])
