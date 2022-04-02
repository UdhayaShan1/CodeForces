n1 = int(input())
list1 = []
for i in (input().split()):
    list1.append(int(i))
 
list2 = []
for i in list1:
    list2.append(i%2)
 
print(min(len([i for i, x in enumerate(list2) if x == 0]), len([i for i, x in enumerate(list2) if x == 1])))
