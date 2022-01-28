x = input().split()
n = int(x[0])
k = int(x[1])
list1 = []
for i in range(n):
    list1.append([])
    for j in range(n):
        list1[i].append(1)
k1 = -1
for i in range(n):
    list1[i][k1] = k - (n-1)
    k1-=1

for i in range(n):
    print(*list1[i])
