n1 = int(input())
list1 = []
x = input().split()
for i in x:
    list1.append(int(i))

row = [0]*max(list1)
count = 0
b1 = False
while b1==False:
    for i in list1:
        if i>=count+1:
            row[count] += 1
    count+=1
    if count==max(list1):
        break

row.reverse()
list2 = []
for i in range(max(list1)):
    list2.append([])
    for j in range(n1):
        list2[i].append(0)


c1 = False
start = -1
while c1==False:
    count = 0
    for i in range(len(list2[start])):
        list2[start][i] = 1
        count+=1
        if count == row[start]:
            break
    start-=1
    if start == -max(list1)-1:
        break


d1 = False
start1 = -1
final = []
while d1==False:
    sum1 = 0
    for i in list2:
        sum1+=i[start1]
    final.append(sum1)
    start1-=1
    if start1 == -n1-1:
        break
print(*final)
