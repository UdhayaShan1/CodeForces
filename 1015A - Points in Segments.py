x = input().split()
list1 = []
for i in range(int(x[0])):
    y = input().split()
    list1 += list(range(int(y[0]),int(y[1])+1))
list2 = []        
for i in range(1,int(x[1])+1):
    if i not in list1:
        list2.append(i)
print(len(list2))        
print(*list2)
