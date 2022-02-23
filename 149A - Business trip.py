n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()
list1 = list1[::-1]
count = 0
sum1 = 0
for i in list1:
    if sum1>=n1:
        break
    sum1+=i
    count+=1
 
if sum1 < n1:
    print(-1)
else:
    print(count)
