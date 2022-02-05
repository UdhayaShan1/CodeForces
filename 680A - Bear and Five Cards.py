x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()

list2 =[]
list3 = []
for i in range(len(list1)-1):
    if list1[i] == list1[i+1]:
        list2.append(list1[i])

for i in range(len(list1)-2):
    if list1[i] == list1[i+1] and list1[i] == list1[i+2]:
        list3.append(list1[i])

sum1 = 0
for i in list2:
    if i*2 > sum1:
        sum1 = i*2
for i in list3:
    if i*3 > sum1:
        sum1 = i*3

print(sum(list1)-sum1)
