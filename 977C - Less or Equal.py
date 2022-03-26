x = input().split()
n = int(x[0])
k = int(x[1])
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
list1.sort()
 
if k == 0:
    if list1[0] == 1:
        print(-1)
    else:
        print(list1[0]-1)
else:
    if k == n:
        print(list1[k-1])
    else:
        if list1[k-1] != list1[k]:
            print(list1[k-1])
        else:
            print(-1)
