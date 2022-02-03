import math
x = input().split()
n = int(x[0])
k = int(x[1])
print(math.ceil((2*n)/k) + math.ceil((5*n)/k) + math.ceil((8*n)/k))
