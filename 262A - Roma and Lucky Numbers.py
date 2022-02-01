x = input().split()
n = int(x[0])
k = int(x[1])

count = 0

x = input().split()
temp = []
for i in x:
    temp.append(int(i))
for i in temp:
    digit = 0
    for j in str(i):
        if int(j) == 4 or int(j) == 7:
            digit+=1
    if digit<=k:
        count+=1
print(count)
