n1 = int(input())
x = input().split()
list1 = []
for i in x:
    list1.append(int(i))
    
index_ones = [i for i, x in enumerate(list1) if x == 1]
print(len(index_ones))
list2 = []
if len(index_ones) == 1:
    list2.append(str(list1[-1]))
else:
    for i in index_ones[1:]:
        list2.append(str(list1[i-1]))
    list2.append(str(list1[-1]))
    
print(' '.join(list2))
