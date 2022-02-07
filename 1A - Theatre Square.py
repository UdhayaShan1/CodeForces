import math
x = input().split()
n = int(x[0])
m = int(x[1])
a = int(x[2])
print(math.ceil(n/a)*math.ceil(m/a))
