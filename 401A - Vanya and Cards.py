import math
x1 = input().split()
n = int(x1[0])
x = int(x1[1])
x2 = input().split()
list1 = []
for i in x2:
    list1.append(int(i))
print(math.ceil(abs(sum(list1))/x))
