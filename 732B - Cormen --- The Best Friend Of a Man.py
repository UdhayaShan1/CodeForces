x = input().split()
n = int(x[0])
k = int(x[1])
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))
count = 0
for i in range(n-1):
    if list1[i] + list1[i+1] < k:
        count += k - (list1[i] + list1[i+1])
        list1[i+1] += k - (list1[i] + list1[i+1])
    else:
        continue

print(count)
print(*list1)
