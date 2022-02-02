n1 = int(input())
list1 = []
for i in range(n1):
    x = input().split()
    l = int(x[0])
    r = int(x[1])
    temp = list(range(l,r+1))
    list1.append(temp)

index = int(input())
count = 0

for i in range(len(list1)):
    if index in list1[i]:
        count = i+1
print(n1-count+1)
