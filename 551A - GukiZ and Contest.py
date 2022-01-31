n1 = int(input())
x = input().split()
list1 = []
for j in x:
    list1.append(int(j))
list2 = []

for i in range(len(list1)):
    count = 0
    for j in range(len(list1)):
        if j != i and list1[j] > list1[i]:
            count+=1
    list2.append(count+1)

print(*list2)
    
