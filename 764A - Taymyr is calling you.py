x = input().split()
n = int(x[0])
m = int(x[1])
z = int(x[2])

list1 = []
for i in range(n,10001,n):
    if i > z:
        break
    list1.append(i)
count = 0
for i in range(m,10001,m):
    if i in list1:
        count+=1
print(count)
