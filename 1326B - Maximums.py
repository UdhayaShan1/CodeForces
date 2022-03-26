n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))
list2 = [list1[0]]
max1 = list2[0]
for i in range(1,n1):
    list2.append(max1 + list1[i])
    if list2[i] > max1:
        max1 = list2[i]
 
print(*list2)
