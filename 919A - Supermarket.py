x = input().split()
n = int(x[0])
m = int(x[1])
min1 = 100000
for i in range(n):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    if m*(a/b) < min1:
        min1 = m*(a/b)
print(min1)
