x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
n = list1[0]
m = list1[1]
a = list1[2]
b = list1[3]
if b/m >=a:
    print(n*a)
else:
    count = (n // m) * b
    n = n % m
    if n*a >= b:
        count+=b
    else:
        count+=n*a
    print(count)
