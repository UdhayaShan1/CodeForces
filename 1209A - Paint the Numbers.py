n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()

count = 0
k1 = 0
b1 = False
while b1==False:
    start = list1[k1]
    temp = []
    for i in range(1,len(list1)):
        if list1[i] % start == 0:
            temp.append(list1[i])
    count += 1
    for i in temp:
        list1.remove(i)
    list1.pop(k1)
    if len(list1) == 0:
        print(count)
        break
