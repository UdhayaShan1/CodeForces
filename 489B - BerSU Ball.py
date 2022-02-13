n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))

n2 = int(input())
x = input().split()
list2 = []
for i in x:
    list2.append(int(i))
list1.sort()
list2.sort()

b1 = False
start = 0
count = 0
while b1==False:
    ref = list1[start]
    ref2 = 0
    flag = 0
    for i in list2:
        if abs(i-ref) <= 1:
            flag+=1
            ref2 = i
            list2.remove(i)
            count+=1
            break
    start+=1
    if start == len(list1):
        print(count)
        break
