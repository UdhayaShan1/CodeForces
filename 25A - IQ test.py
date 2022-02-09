x = int(input())
list1 = []
y = input().split()
for i in y:
    list1.append(int(i))

even = 0
odd = 0
for i in list1[0:3]:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
if even>odd:
    print([i for i, x in enumerate(list1) if x % 2 != 0][0]+1)
else:
    print([i for i, x in enumerate(list1) if x % 2 == 0][0]+1)
