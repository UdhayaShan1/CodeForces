x = input().split()
temp = input().split()
list1 = []
for i in temp:
    list1.append(int(i))
n = int(x[0])
m = int(x[1])
b1 = False
start = 0
list2 = []
for i in range(1,n+1):
    list2.append(i)
 
while b1==False:
    if m >= list1[0]:
        if len(list1) == 1:
            break
        list1.pop(0)
        list2.pop(0)
        continue
    if list1[0] > m:
        if len(list1) == 1:
            break
        list1[0] = list1[0] - m
        temp1 = list1[0]
        temp2 = list2[0]
        list1.pop(0)
        list1.append(temp1)
        list2.pop(0)
        list2.append(temp2)
        continue
 
print(list2[-1])
