n1 = int(input())
m = int(input())
list1 = []
for i in range(n1):
    list1.append(int(input()))

list1.sort()
list1 = list1[::-1]
count = 0
for i in list1:
    if m <= 0:
        break
    count+=1
    m-=i

print(count)
