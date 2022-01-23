import math
x = input().split()
n = int(x[0])
k = int(x[1])
str1 = "abcdefghijklmnopqrstuvwxyz"

list1 = []
y = str1[0:k]
list1.append(y)
remain = math.ceil((n-k) / len(y))
temp = y * remain
list1.append(temp[0:(n-k)])

print(''.join(list1))
