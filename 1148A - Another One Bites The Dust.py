x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
x = 0
if max(a,b) - min(a,b) > 0:
    x = 1
else:
    x = 0
print(2*c + 2*min(a,b) + x)
