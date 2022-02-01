x = input().split()
n = int(x[0])
m = int(x[1])
list1 = []
for i in range(n):
    x = input().split()
    temp = []
    for j in x:
        temp.append(int(j))
    list1 += temp[1:]

if len(set(list1)) == m:
    print("YES")
else:
    print("NO")
