x = input().split()
n = int(x[0])
m = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
 
list2 = []
for i in list1:
    if i < 0:
        list2.append(-i)
list2.sort()
list2.reverse()
list3 = []
 
count = 0
sum1 = 0
for i in list2:
    if count == m:
        break
    sum1+=i
    count+=1
 
print(abs(sum1))
